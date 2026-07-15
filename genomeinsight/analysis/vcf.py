"""
Variant analysis functions for GenomeInsight.
"""
from collections import Counter

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

def extract_indels(variants):
    """
    Extract insertion and deletion variants.

    Parameters
    ----------
    variants : list
        Parsed VCF variants.

    Returns
    -------
    list
        INDEL variants.
    """

    indels = []

    for variant in variants:
        ref = variant["ref"]
        alt = variant["alt"]

        if len(ref) != len(alt):
            if len(alt) > len(ref):
                variant_type = "Insertion"
            else:
                variant_type = "Deletion"

            indels.append(
                {
                    "chrom": variant["chrom"],
                    "pos": variant["pos"],
                    "ref": ref,
                    "alt": alt,
                    "type": variant_type,
                }
            )

    return indels

def chromosome_statistics(variants):
    """
    Count variants per chromosome.

    Parameters
    ----------
    variants : list
        Parsed VCF variants.

    Returns
    -------
    dict
        Chromosome -> variant count.
    """

    counts = Counter()

    for variant in variants:
        counts[variant["chrom"]] += 1

    return dict(counts)

def generate_summary(variants):
    """
    Generate a complete summary of VCF variants.

    Parameters
    ----------
    variants : list
        Parsed VCF variants.

    Returns
    -------
    dict
        Combined VCF summary.
    """

    return {
        "statistics": variant_statistics(variants),
        "chromosomes": chromosome_statistics(variants),
    }

def transition_transversion_ratio(variants):
    """
    Calculate transition and transversion statistics.

    Parameters
    ----------
    variants : list
        Parsed VCF variants.

    Returns
    -------
    dict
        Transition/transversion statistics.
    """

    transitions = {
        ("A", "G"),
        ("G", "A"),
        ("C", "T"),
        ("T", "C"),
    }

    ts = 0
    tv = 0

    for variant in variants:
        ref = variant["ref"]
        alt = variant["alt"]

        # Only SNPs are considered
        if len(ref) != 1 or len(alt) != 1:
            continue

        if (ref, alt) in transitions:
            ts += 1
        else:
            tv += 1

    ratio = ts / tv if tv else None

    return {
        "transitions": ts,
        "transversions": tv,
        "ratio": ratio,
    }

def filter_variants(
    variants,
    chromosome=None,
    variant_type=None,
):
    """
    Filter variants by chromosome and/or type.

    Parameters
    ----------
    variants : list
        Parsed VCF variants.

    chromosome : str, optional
        Chromosome name.

    variant_type : str, optional
        "snp" or "indel".

    Returns
    -------
    list
        Filtered variants.
    """

    filtered = []

    for variant in variants:

        if chromosome is not None:
            if variant["chrom"] != chromosome:
                continue

        if variant_type == "snp":
            if not (
                len(variant["ref"]) == 1
                and len(variant["alt"]) == 1
            ):
                continue

        elif variant_type == "indel":
            if len(variant["ref"]) == len(variant["alt"]):
                continue

        filtered.append(variant)

    return filtered