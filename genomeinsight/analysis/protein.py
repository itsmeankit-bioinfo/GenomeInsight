"""
Protein sequence analysis utilities.

This module provides functions for analyzing protein sequences
using BioPython's ProtParam module.
"""

from Bio.SeqUtils.ProtParam import ProteinAnalysis


def analyze_protein(sequence: str) -> dict:
    """
    Perform comprehensive protein analysis.

    Parameters
    ----------
    sequence : str
        Protein sequence.

    Returns
    -------
    dict
        Dictionary containing protein statistics.
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
        "amino_acid_composition": analysis.count_amino_acids(),
    }


def amino_acid_composition(sequence: str) -> dict:
    """
    Return amino acid composition.

    Parameters
    ----------
    sequence : str
        Protein sequence.

    Returns
    -------
    dict
        Amino acid counts.
    """

    sequence = sequence.upper()

    analysis = ProteinAnalysis(sequence)

    return analysis.count_amino_acids()


def molecular_weight(sequence: str) -> float:
    """
    Calculate molecular weight.

    Parameters
    ----------
    sequence : str
        Protein sequence.

    Returns
    -------
    float
        Molecular weight (Da).
    """

    return round(
        ProteinAnalysis(sequence.upper()).molecular_weight(),
        2,
    )


def isoelectric_point(sequence: str) -> float:
    """
    Calculate isoelectric point (pI).

    Parameters
    ----------
    sequence : str
        Protein sequence.

    Returns
    -------
    float
        Isoelectric point.
    """

    return round(
        ProteinAnalysis(sequence.upper()).isoelectric_point(),
        2,
    )


def aromaticity(sequence: str) -> float:
    """
    Calculate aromaticity.

    Parameters
    ----------
    sequence : str
        Protein sequence.

    Returns
    -------
    float
        Aromaticity score.
    """

    return round(
        ProteinAnalysis(sequence.upper()).aromaticity(),
        4,
    )


def instability_index(sequence: str) -> float:
    """
    Calculate instability index.

    Parameters
    ----------
    sequence : str
        Protein sequence.

    Returns
    -------
    float
        Instability index.
    """

    return round(
        ProteinAnalysis(sequence.upper()).instability_index(),
        2,
    )


def gravy(sequence: str) -> float:
    """
    Calculate GRAVY (hydrophobicity).

    Parameters
    ----------
    sequence : str
        Protein sequence.

    Returns
    -------
    float
        GRAVY score.
    """

    return round(
        ProteinAnalysis(sequence.upper()).gravy(),
        3,
    )