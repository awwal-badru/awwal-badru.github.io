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
        # Fetch up to 100 free proxies
        url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=5000&country=all&ssl=all&anonymity=all"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req).read().decode('utf-8')
        proxies = [line.strip() for line in res.splitlines() if line.strip()]
        print(f"Retrieved {len(proxies)} proxies from proxyscrape.")
    except Exception as pe:
        print(f"Could not retrieve proxy list: {pe}")

    if not proxies:
        raise ValueError("Failed to fetch Google Scholar profile because no proxies could be retrieved.")

    # Try rotating through the proxies (limit to first 30 to prevent long runs)
    max_proxies_to_try = min(len(proxies), 30)
    for idx, proxy in enumerate(proxies[:max_proxies_to_try]):
        print(f"Trying proxy {idx + 1}/{max_proxies_to_try}: {proxy}")
        try:
            pg = ProxyGenerator()
            pg.SingleProxy(http=f"http://{proxy}", https=f"http://{proxy}")
            scholarly.use_proxy(pg)
            scholarly.set_timeout(5)
            
            author = scholarly.search_author_id(GOOGLE_SCHOLAR_ID)
            if author:
                # Set a slightly larger timeout for filling detailed publication data
                scholarly.set_timeout(8)
                filled_author = scholarly.fill(author)
                print(f"Successfully fetched and filled profile using proxy: {proxy}!")
                return filled_author
        except Exception as e:
            print(f"Proxy {proxy} failed: {e}")
            
    raise ValueError(f"Failed to fetch Google Scholar profile for ID {GOOGLE_SCHOLAR_ID} after trying all available methods.")

def main():
    print(f"Fetching Google Scholar profile for ID: {GOOGLE_SCHOLAR_ID}")
    try:
        author = fetch_profile_with_retry()
    except Exception as err:
        print(f"Failed to fetch profile after multiple attempts: {err}")
        print("Exiting gracefully to prevent breaking CI workflows.")
        return

    # Use flexible lookups for citedby/hindex/i10index properties to handle scholarly library updates
    citations = author.get("citedby", author.get("cited_by", 0))
    h_index = author.get("hindex", author.get("h_index", 0))
    i10_index = author.get("i10index", author.get("i10_index", 0))

    print(f"Citations: {citations}, h-index: {h_index}, i10-index: {i10_index}")

    # Get top cited papers (up to 5)
    pubs = author.get("publications", [])
    papers = []
    
    # Sort publications by citation count
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
            
            # Clean paper title (remove newlines and multiple spaces)
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
        "last_updated": date.today().isoformat(),
        "papers": papers,
    }

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

