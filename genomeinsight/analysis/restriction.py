"""
Restriction enzyme search.
"""

ENZYMES = {
    "EcoRI": "GAATTC",
    "BamHI": "GGATCC",
    "HindIII": "AAGCTT",
    "PstI": "CTGCAG",
    "XhoI": "CTCGAG",
    "NotI": "GCGGCCGC",
}


def find_restriction_sites(sequence: str):
    sequence = sequence.upper()

    results = []

    for enzyme, site in ENZYMES.items():

        start = 0

        while True:

            index = sequence.find(site, start)

            if index == -1:
                break

            results.append({
                "enzyme": enzyme,
                "site": site,
                "position": index + 1
            })

            start = index + 1

    return sorted(results, key=lambda x: x["position"])