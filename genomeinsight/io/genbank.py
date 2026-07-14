"""
GenBank file reader.
"""
from collections import Counter

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

def read_cds(file_path: str) -> list:
    """
    Read all CDS annotations from a GenBank file.
    """

    record = SeqIO.read(file_path, "genbank")

    cds_list = []

    for feature in record.features:
        if feature.type == "CDS":
            cds_list.append(
                {
                    "gene": feature.qualifiers.get(
                        "gene",
                        ["Unknown"],
                    )[0],
                    "product": feature.qualifiers.get(
                        "product",
                        ["Unknown"],
                    )[0],
                    "location": str(feature.location),
                }
            )

    return cds_list

def read_proteins(file_path: str) -> list:
    """
    Read translated protein information from a GenBank file.

    Parameters
    ----------
    file_path : str
        Path to a GenBank file.

    Returns
    -------
    list
        Protein annotations.
    """

    record = SeqIO.read(file_path, "genbank")

    proteins = []

    for feature in record.features:
        if feature.type == "CDS":
            proteins.append(
                {
                    "gene": feature.qualifiers.get(
                        "gene",
                        ["Unknown"],
                    )[0],
                    "protein_id": feature.qualifiers.get(
                        "protein_id",
                        ["Unknown"],
                    )[0],
                    "product": feature.qualifiers.get(
                        "product",
                        ["Unknown"],
                    )[0],
                }
            )

    return proteins


def read_features(file_path: str) -> dict:
    """
    Count feature types in a GenBank file.

    Parameters
    ----------
    file_path : str
        Path to a GenBank file.

    Returns
    -------
    dict
        Feature counts.
    """

    record = SeqIO.read(file_path, "genbank")

    counter = Counter()

    for feature in record.features:
        counter[feature.type] += 1

    return dict(counter)