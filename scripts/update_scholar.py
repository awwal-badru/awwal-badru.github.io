"""
Fetch Google Scholar metrics for Awwal Badru and update _data/scholar.yml.

Uses the `scholarly` library to scrape the public Google Scholar profile.
This script is called by the GitHub Actions workflow (.github/workflows/update-scholar.yml).
"""

import yaml
import time
from datetime import date
import scholarly as scholarly_module
from scholarly import ProxyGenerator

scholarly = scholarly_module.scholarly

GOOGLE_SCHOLAR_ID = "DW7LA8sAAAAJ"
OUTPUT_FILE = "_data/scholar.yml"

def fetch_profile_with_retry(max_retries=3):
    """Fetch the author profile, retrying with proxy fallback if needed."""
    use_proxy_next = False
    
    for attempt in range(1, max_retries + 1):
        print(f"Attempt {attempt} of {max_retries} to fetch profile (use_proxy={use_proxy_next})...")
        try:
            if use_proxy_next:
                try:
                    print("Setting up Free Proxies...")
                    pg = ProxyGenerator()
                    pg.FreeProxies()
                    scholarly.use_proxy(pg)
                except Exception as pe:
                    print(f"Could not initialize proxy generator: {pe}. Proceeding without proxy.")
            
            author = scholarly.search_author_id(GOOGLE_SCHOLAR_ID)
            if not author:
                raise ValueError(f"No author found for ID: {GOOGLE_SCHOLAR_ID}")
                
            author = scholarly.fill(author)
            return author
            
        except Exception as e:
            print(f"Error on attempt {attempt}: {e}")
            if attempt < max_retries:
                # Next attempt will try with proxy
                use_proxy_next = True
                sleep_time = attempt * 5
                print(f"Waiting {sleep_time} seconds before retrying...")
                time.sleep(sleep_time)
            else:
                raise e

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

