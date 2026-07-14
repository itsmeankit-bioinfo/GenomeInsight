"""
GenBank file reader.
"""

from Bio import SeqIO


def read_genbank(file_path: str) -> dict:
    """
    Read a GenBank file and return basic information.

    Parameters
    ----------
    file_path : str
        Path to a GenBank file.

    Returns
    -------
    dict
        Parsed GenBank information.
    """

    record = SeqIO.read(file_path, "genbank")

    return {
        "id": record.id,
        "name": record.name,
        "description": record.description,
        "organism": record.annotations.get(
            "organism",
            "Unknown",
        ),
        "length": len(record.seq),
        "molecule_type": record.annotations.get(
            "molecule_type",
            "Unknown",
        ),
        "topology": record.annotations.get(
            "topology",
            "Unknown",
        ),
    }

def read_genes(file_path: str) -> list:
    """
    Read all gene annotations from a GenBank file.

    Parameters
    ----------
    file_path : str
        Path to a GenBank file.

    Returns
    -------
    list
        List of genes.
    """

    record = SeqIO.read(file_path, "genbank")

    genes = []

    for feature in record.features:
        if feature.type == "gene":
            genes.append(
                {
                    "gene": feature.qualifiers.get(
                        "gene",
                        ["Unknown"],
                    )[0],
                    "location": str(feature.location),
                }
            )

    return genes
