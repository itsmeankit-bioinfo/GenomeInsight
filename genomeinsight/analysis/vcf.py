"""
Variant analysis functions for GenomeInsight.
"""


def variant_statistics(variants):
    """
    Calculate basic statistics from VCF variants.
    """

    chromosomes = set()
    snps = 0
    insertions = 0
    deletions = 0

    for variant in variants:
        chromosomes.add(variant["chrom"])

        ref = variant["ref"]
        alt = variant["alt"]

        if len(ref) == 1 and len(alt) == 1:
            snps += 1
        elif len(alt) > len(ref):
            insertions += 1
        elif len(ref) > len(alt):
            deletions += 1

    return {
        "variants": len(variants),
        "chromosomes": len(chromosomes),
        "snps": snps,
        "insertions": insertions,
        "deletions": deletions,
    }

def extract_snps(variants):
    """
    Extract SNP variants.

    Parameters
    ----------
    variants : list
        Parsed VCF variants.

    Returns
    -------
    list
        SNP variants.
    """

    snps = []

    for variant in variants:
        if (
            len(variant["ref"]) == 1
            and len(variant["alt"]) == 1
        ):
            snps.append(variant)

    return snps