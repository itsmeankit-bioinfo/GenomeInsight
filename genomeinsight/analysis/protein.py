"""
Protein sequence analysis utilities.
"""

from Bio.SeqUtils.ProtParam import ProteinAnalysis


def protein_info(sequence: str) -> dict:
    """
    Analyze a protein sequence.

    Parameters
    ----------
    sequence : str
        Protein sequence.

    Returns
    -------
    dict
        Protein statistics.
    """

    sequence = sequence.upper()

    analysis = ProteinAnalysis(sequence)

    return {
        "length": len(sequence),
        "molecular_weight": round(
            analysis.molecular_weight(),
            2,
        ),
        "isoelectric_point": round(
            analysis.isoelectric_point(),
            2,
        ),
        "aromaticity": round(
            analysis.aromaticity(),
            4,
        ),
        "instability_index": round(
            analysis.instability_index(),
            2,
        ),
        "gravy": round(
            analysis.gravy(),
            3,
        ),
        "amino_acids": analysis.count_amino_acids(),
    }