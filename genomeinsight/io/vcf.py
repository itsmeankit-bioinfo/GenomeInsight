"""
VCF parser for GenomeInsight.
"""


def read_vcf(file_path: str) -> list:
    """
    Read variants from a VCF file.

    Parameters
    ----------
    file_path : str
        Path to a VCF file.

    Returns
    -------
    list
        Variant records.
    """

    variants = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if line.startswith("#"):
                continue

            fields = line.strip().split("\t")

            variants.append(
                {
                    "chrom": fields[0],
                    "pos": int(fields[1]),
                    "ref": fields[3],
                    "alt": fields[4],
                }
            )

    return variants