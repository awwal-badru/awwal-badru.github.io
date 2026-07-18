"""
Fetch Google Scholar metrics for Awwal Badru and update _data/scholar.yml.

Uses the `scholarly` library to scrape the public Google Scholar profile.
This script is called by the GitHub Actions workflow (.github/workflows/update-scholar.yml).
"""

import yaml
import time
import urllib.request
from datetime import date
import scholarly as scholarly_module
from scholarly import ProxyGenerator

scholarly = scholarly_module.scholarly

GOOGLE_SCHOLAR_ID = "DW7LA8sAAAAJ"
OUTPUT_FILE = "_data/scholar.yml"

def fetch_profile_with_retry():
    """Fetch the author profile, retrying with public proxy rotation if blocked."""
    # First attempt: Try directly without proxy (useful for local runs)
    print("Attempting to fetch profile directly without proxy...")
    try:
        scholarly.set_timeout(5)
        author = scholarly.search_author_id(GOOGLE_SCHOLAR_ID)
        if author:
            print("Successfully fetched profile directly without proxy!")
            return scholarly.fill(author)
    except Exception as e:
        print(f"Direct fetch failed: {e}. Moving to proxy rotation.")

    # Second attempt: Fetch fresh public proxies and try them
    print("Fetching active proxy list from proxyscrape...")
    proxies = []
    try:
        # Fetch high-quality SSL-enabled elite anonymous proxies
        url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=3000&country=all&ssl=yes&anonymity=elite"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req).read().decode('utf-8')
        proxies = [line.strip() for line in res.splitlines() if line.strip()]
        print(f"Retrieved {len(proxies)} proxies from proxyscrape.")
    except Exception as pe:
        print(f"Could not retrieve proxy list: {pe}")

    if not proxies:
        raise ValueError("Failed to fetch Google Scholar profile because no proxies could be retrieved.")

    # Try rotating through the proxies (limit to first 15 to prevent long runs)
    max_proxies_to_try = min(len(proxies), 15)
    for idx, proxy in enumerate(proxies[:max_proxies_to_try]):
        print(f"Trying proxy {idx + 1}/{max_proxies_to_try}: {proxy}")
        try:
            pg = ProxyGenerator()
            pg.SingleProxy(http=f"http://{proxy}", https=f"http://{proxy}")
            scholarly.use_proxy(pg)
            scholarly.set_timeout(3)
            
            author = scholarly.search_author_id(GOOGLE_SCHOLAR_ID)
            if author:
                # Set a slightly larger timeout for filling detailed publication data
                scholarly.set_timeout(5)
                filled_author = scholarly.fill(author)
                print(f"Successfully fetched and filled profile using proxy: {proxy}!")
                return filled_author
        except Exception as e:
            print(f"Proxy {proxy} failed: {e}")
            
    raise ValueError(f"Failed to fetch Google Scholar profile for ID {GOOGLE_SCHOLAR_ID} after trying all available methods.")

def fetch_profile_with_serpapi(api_key):
    """Fetch the author profile and citation details using SerpApi."""
    print("Attempting to fetch profile using SerpApi...")
    import json
    import urllib.parse
    import urllib.request

    params = {
        "engine": "google_scholar_author",
        "author_id": GOOGLE_SCHOLAR_ID,
        "api_key": api_key,
    }
    url = f"https://serpapi.com/search.json?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            results = json.loads(response.read().decode('utf-8'))
            
            # Extract citation stats
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
            
            # Extract top cited papers
            articles = results.get("articles", [])
            papers = []
            
            # Sort publications by citation count
            sorted_articles = sorted(articles, key=lambda a: a.get("cited_by", {}).get("value", 0), reverse=True)[:5]
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
                    
            print(f"Successfully fetched profile using SerpApi! Citations: {citations}, h-index: {h_index}, i10-index: {i10_index}")
            return {
                "citations": citations,
                "h_index": h_index,
                "i10_index": i10_index,
                "papers": papers
            }
    except Exception as e:
        print(f"SerpApi fetch failed: {e}")
        raise

def main():
    import os
    print(f"Fetching Google Scholar profile for ID: {GOOGLE_SCHOLAR_ID}")
    
    serpapi_key = os.environ.get("SERPAPI_KEY")
    data = None
    
    if serpapi_key:
        try:
            data = fetch_profile_with_serpapi(serpapi_key)
        except Exception as err:
            print(f"SerpApi failed, falling back to direct/proxy scraping: {err}")
            
    if data is None:
        try:
            author = fetch_profile_with_retry()
            citations = author.get("citedby", author.get("cited_by", 0))
            h_index = author.get("hindex", author.get("h_index", 0))
            i10_index = author.get("i10index", author.get("i10_index", 0))
            print(f"Citations: {citations}, h-index: {h_index}, i10-index: {i10_index}")

            pubs = author.get("publications", [])
            papers = []
            sorted_pubs = sorted(pubs, key=lambda p: p.get("num_citations", 0), reverse=True)[:5]
            
            for pub in sorted_pubs:
                citations_count = pub.get("num_citations", 0)
                if citations_count > 0:
                    bib = pub.get("bib", {})
                    cid = pub.get("author_pub_id", "")
                    url = (
                        f"https://scholar.google.com/citations?view_op=view_citation"
                        f"&hl=en&user={GOOGLE_SCHOLAR_ID}&citation_for_view={cid}"
                    )
                    title = bib.get("title", "Untitled")
                    title_clean = " ".join(title.split())
                    
                    papers.append({
                        "title": title_clean,
                        "citations": citations_count,
                        "url": url,
                    })
            data = {
                "citations": citations,
                "h_index": h_index,
                "i10_index": i10_index,
                "papers": papers,
            }
        except Exception as err:
            print(f"Failed to fetch profile after multiple attempts: {err}")
            print("Exiting gracefully to prevent breaking CI workflows.")
            return

    data["last_updated"] = date.today().isoformat()

    header = (
        "# Google Scholar citation metrics for Awwal Badru\n"
        f"# Google Scholar ID: {GOOGLE_SCHOLAR_ID}\n"
        "# Auto-updated by GitHub Actions (see .github/workflows/update-scholar.yml)\n\n"
    )

    try:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(header)
            # Use width=1000 to prevent YAML from wrapping long titles
            yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=1000)
        print(f"Updated {OUTPUT_FILE}")
    except Exception as write_err:
        print(f"Error writing to output file: {write_err}")

if __name__ == "__main__":
    main()


