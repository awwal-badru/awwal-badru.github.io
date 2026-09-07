"""
Fetch Google Scholar metrics for Awwal Badru and update _data/scholar.yml.

Uses robust direct scraping of the public Google Scholar profile with fallback
to the Google Scholar pagination endpoint and optional SerpApi.
This script is called by the GitHub Actions workflow (.github/workflows/update-scholar.yml).
"""

import os
import re
import sys
import yaml
import json
import urllib.request
import urllib.parse
from datetime import date

GOOGLE_SCHOLAR_ID = "DW7LA8sAAAAJ"
OUTPUT_FILE = "_data/scholar.yml"
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
)

def fetch_profile_direct():
    """
    Fetch the public Google Scholar profile page directly with browser headers.
    Extracts citation metrics (total citations, h-index, i10-index) and papers.
    """
    print("Attempting direct fetch of Google Scholar profile...")
    url = f"https://scholar.google.com/citations?user={GOOGLE_SCHOLAR_ID}&hl=en"
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    }
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as response:
        html = response.read().decode("utf-8")

    # Verify we didn't receive a CAPTCHA page
    if "Please show you&#39;re not a robot" in html or "recaptcha" in html.lower():
        raise RuntimeError("Google Scholar presented a CAPTCHA challenge.")

    # Citation table contains: Citations (All, Since), h-index (All, Since), i10-index (All, Since)
    matches = re.findall(r'<td class="gsc_rsb_std">(\d+)</td>', html)
    if not matches:
        raise ValueError("Could not find citation statistics in profile HTML.")

    if len(matches) >= 6:
        citations = int(matches[0])
        h_index = int(matches[2])
        i10_index = int(matches[4])
    elif len(matches) >= 3:
        citations = int(matches[0])
        h_index = int(matches[1])
        i10_index = int(matches[2])
    else:
        raise ValueError(f"Unexpected number of stats matches: {len(matches)}")

    # Extract papers from <tr class="gsc_a_tr">
    paper_rows = re.findall(r'<tr class="gsc_a_tr">(.*?)</tr>', html, re.DOTALL)
    papers = []
    for row in paper_rows:
        title_match = re.search(
            r'<a[^>]+href="([^"]*citation_for_view=[^"]*)"[^>]*class="gsc_a_at"[^>]*>(.*?)</a>',
            row,
            re.DOTALL,
        )
        cites_match = re.search(
            r'<td class="gsc_a_c">.*?<a[^>]*class="gsc_a_ac[^"]*"[^>]*>(\d*)</a>',
            row,
            re.DOTALL,
        )

        if title_match:
            raw_url = title_match.group(1).replace("&amp;", "&")
            p_url = "https://scholar.google.com" + raw_url if raw_url.startswith("/") else raw_url
            p_title = re.sub(r"<[^>]+>", "", title_match.group(2)).strip()
            # Normalize whitespace in title
            p_title = " ".join(p_title.split())
            p_cites = (
                int(cites_match.group(1))
                if (cites_match and cites_match.group(1).isdigit())
                else 0
            )

            # Only include papers with at least 1 citation in the most-cited list
            if p_cites > 0:
                papers.append({
                    "title": p_title,
                    "citations": p_cites,
                    "url": p_url,
                })

    # Sort papers descending by citation count and take top 5
    papers = sorted(papers, key=lambda p: p["citations"], reverse=True)[:5]

    return {
        "citations": citations,
        "h_index": h_index,
        "i10_index": i10_index,
        "papers": papers,
    }

def fetch_profile_post_endpoint():
    """
    Fallback: Fetch papers via Google Scholar's POST pagination endpoint.
    Used if the main page structure changes.
    """
    print("Attempting POST endpoint fetch of Google Scholar records...")
    url = f"https://scholar.google.com/citations?user={GOOGLE_SCHOLAR_ID}&cstart=0&pagesize=100"
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
    }
    req = urllib.request.Request(url, data=b"json=1", headers=headers)
    with urllib.request.urlopen(req, timeout=15) as response:
        res = json.loads(response.read().decode("utf-8"))

    html = res.get("B", "")
    if not html:
        raise ValueError("POST endpoint returned empty HTML body.")

    paper_rows = re.findall(r'<tr class="gsc_a_tr">(.*?)</tr>', html, re.DOTALL)
    papers = []
    for row in paper_rows:
        title_match = re.search(
            r'<a[^>]+href="([^"]*citation_for_view=[^"]*)"[^>]*class="gsc_a_at"[^>]*>(.*?)</a>',
            row,
            re.DOTALL,
        )
        cites_match = re.search(
            r'<td class="gsc_a_c">.*?<a[^>]*class="gsc_a_ac[^"]*"[^>]*>(\d*)</a>',
            row,
            re.DOTALL,
        )
        if title_match:
            raw_url = title_match.group(1).replace("&amp;", "&")
            p_url = "https://scholar.google.com" + raw_url if raw_url.startswith("/") else raw_url
            p_title = re.sub(r"<[^>]+>", "", title_match.group(2)).strip()
            p_title = " ".join(p_title.split())
            p_cites = (
                int(cites_match.group(1))
                if (cites_match and cites_match.group(1).isdigit())
                else 0
            )
            if p_cites > 0:
                papers.append({
                    "title": p_title,
                    "citations": p_cites,
                    "url": p_url,
                })

    papers = sorted(papers, key=lambda p: p["citations"], reverse=True)[:5]
    return papers

def fetch_profile_with_serpapi(api_key):
    """
    Fetch the author profile and citation details using SerpApi (if configured).
    """
    print("Attempting to fetch profile using SerpApi...")
    params = {
        "engine": "google_scholar_author",
        "author_id": GOOGLE_SCHOLAR_ID,
        "api_key": api_key,
    }
    url = f"https://serpapi.com/search.json?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})

    with urllib.request.urlopen(req, timeout=15) as response:
        results = json.loads(response.read().decode("utf-8"))

    cited_by_table = results.get("cited_by", {}).get("table", [])
    citations = 0
    h_index = 0
    i10_index = 0
    for row in cited_by_table:
        if "citations" in row:
            citations = row["citations"].get("all", 0)
        elif "h_index" in row:
            h_index = row["h_index"].get("all", 0)
        elif "i10_index" in row:
            i10_index = row["i10_index"].get("all", 0)

    articles = results.get("articles", [])
    papers = []
    sorted_articles = sorted(
        articles,
        key=lambda a: a.get("cited_by", {}).get("value", 0),
        reverse=True,
    )[:5]
    for art in sorted_articles:
        citations_count = art.get("cited_by", {}).get("value", 0)
        if citations_count > 0:
            title = art.get("title", "Untitled")
            title_clean = " ".join(title.split())
            url = art.get("link", "")
            papers.append({
                "title": title_clean,
                "citations": citations_count,
                "url": url,
            })

    return {
        "citations": citations,
        "h_index": h_index,
        "i10_index": i10_index,
        "papers": papers,
    }

def read_existing_data():
    """Read the current scholar.yml if present."""
    if os.path.exists(OUTPUT_FILE):
        try:
            with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
                return yaml.safe_load(f) or {}
        except Exception as e:
            print(f"Warning: could not read existing {OUTPUT_FILE}: {e}")
    return {}

def main():
    print(f"Starting Google Scholar metric update for author ID: {GOOGLE_SCHOLAR_ID}")
    existing = read_existing_data()
    existing_citations = existing.get("citations", 0)
    print(f"Current recorded citations in {OUTPUT_FILE}: {existing_citations}")

    data = None

    # Method 1: Check if SerpApi key is provided
    serpapi_key = os.environ.get("SERPAPI_KEY", "").strip()
    if serpapi_key:
        try:
            data = fetch_profile_with_serpapi(serpapi_key)
            print("Successfully fetched metrics via SerpApi.")
        except Exception as e:
            print(f"SerpApi fetch failed: {e}. Falling back to direct fetch.")

    # Method 2: Direct profile page scraping
    if data is None:
        try:
            data = fetch_profile_direct()
            print("Successfully fetched metrics via direct profile scrape.")
        except Exception as e:
            print(f"Direct profile fetch failed: {e}.")

    # Method 3: If direct fetch failed to get papers, try POST endpoint
    if data is not None and not data.get("papers"):
        try:
            papers = fetch_profile_post_endpoint()
            if papers:
                data["papers"] = papers
                print(f"Retrieved {len(papers)} papers via POST endpoint fallback.")
        except Exception as e:
            print(f"POST endpoint fallback failed: {e}.")

    # Validation
    if not data or data.get("citations", 0) == 0:
        print("ERROR: Failed to retrieve valid Google Scholar metrics.")
        # If we failed to get new data, fail with error code so CI registers failure
        # rather than silently continuing.
        sys.exit(1)

    print(f"Fetched Metrics -> Citations: {data['citations']}, h-index: {data['h_index']}, i10-index: {data['i10_index']}")
    print(f"Fetched {len(data.get('papers', []))} top papers.")

    # Safety check: prevent overwriting with significantly lower citations (e.g. scrape glitch)
    if data["citations"] < existing_citations:
        print(f"WARNING: Fetched citations ({data['citations']}) is less than existing citations ({existing_citations}). Skipping update to preserve data integrity.")
        sys.exit(0)

    data["last_updated"] = date.today().isoformat()

    header = (
        "# Google Scholar citation metrics for Awwal Badru\n"
        f"# Google Scholar ID: {GOOGLE_SCHOLAR_ID}\n"
        "# Auto-updated by GitHub Actions (see .github/workflows/update-scholar.yml)\n\n"
    )

    try:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(header)
            yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=1000)
        print(f"Successfully updated {OUTPUT_FILE}!")
    except Exception as write_err:
        print(f"Error writing to output file: {write_err}")
        sys.exit(1)

if __name__ == "__main__":
    main()
