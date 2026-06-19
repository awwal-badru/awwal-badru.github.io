"""
Fetch Google Scholar metrics for Awwal Badru and update _data/scholar.yml.

Uses the `scholarly` library to scrape the public Google Scholar profile.
This script is called by the GitHub Actions workflow (.github/workflows/update-scholar.yml).
"""

import yaml
from datetime import date
from scholarly import scholarly

GOOGLE_SCHOLAR_ID = "DW7LA8sAAAAJ"
OUTPUT_FILE = "_data/scholar.yml"

def main():
    print(f"Fetching Google Scholar profile for ID: {GOOGLE_SCHOLAR_ID}")
    author = scholarly.search_author_id(GOOGLE_SCHOLAR_ID)
    author = scholarly.fill(author)

    citations = author.get("citedby", 0)
    h_index = author.get("hindex", 0)
    i10_index = author.get("i10index", 0)

    print(f"Citations: {citations}, h-index: {h_index}, i10-index: {i10_index}")

    # Get top cited papers (up to 5)
    pubs = author.get("publications", [])
    papers = []
    for pub in sorted(pubs, key=lambda p: p.get("num_citations", 0), reverse=True)[:5]:
        if pub.get("num_citations", 0) > 0:
            bib = pub.get("bib", {})
            cid = pub.get("author_pub_id", "")
            url = (
                f"https://scholar.google.com/citations?view_op=view_citation"
                f"&hl=en&user={GOOGLE_SCHOLAR_ID}&citation_for_view={cid}"
            )
            papers.append({
                "title": bib.get("title", "Untitled"),
                "citations": pub["num_citations"],
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

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(header)
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    print(f"Updated {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
