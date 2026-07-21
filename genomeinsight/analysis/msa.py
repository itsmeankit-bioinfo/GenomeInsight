"""
Multiple Sequence Alignment (MSA) utilities.

This module provides helper functions for reading and validating
multiple sequence FASTA files.
"""

from Bio import SeqIO
from collections import Counter


VALID_NUCLEOTIDES = {"A", "T", "G", "C", "N", "-"}


def validate_minimum_sequences(sequences):
    """
    Ensure at least two sequences are provided.
    """
    if len(sequences) < 2:
        raise ValueError("At least two sequences are required.")


def validate_duplicate_ids(sequences):
    """
    Ensure sequence IDs are unique.
    """
    ids = [seq.id for seq in sequences]

    duplicates = [
        seq_id
        for seq_id, count in Counter(ids).items()
        if count > 1
    ]

    if duplicates:
        raise ValueError(
            f"Duplicate sequence IDs found: {', '.join(duplicates)}"
        )


def validate_nucleotide_sequences(sequences):
    """
    Ensure sequences contain only valid nucleotide characters.
    """

    for seq in sequences:
        sequence = str(seq.seq).upper()

        invalid = set(sequence) - VALID_NUCLEOTIDES

        if invalid:
            raise ValueError(
                f"Invalid nucleotide(s) in {seq.id}: "
                f"{', '.join(sorted(invalid))}"
            )


def validate_sequences(sequences):
    """
    Run all sequence validation checks.
    """

    validate_minimum_sequences(sequences)
    validate_duplicate_ids(sequences)
    validate_nucleotide_sequences(sequences)


def read_sequences(file_path):
    """
    Read all sequences from a FASTA file.

    Parameters
    ----------
    file_path : str
        Path to FASTA file.

    Returns
    -------
    list
        List of SeqRecord objects.

    Raises
    ------
    ValueError
        If no sequences are found.
    """

    sequences = list(SeqIO.parse(file_path, "fasta"))

    if not sequences:
        raise ValueError("No sequences found in FASTA file.")

    return sequences

def score(a, b, match=1, mismatch=-1):
    """
    Return match or mismatch score.
    """
    return match if a == b else mismatch

def initialize_matrix(rows, cols, gap=-1):
    """
    Create and initialize the Needleman–Wunsch score matrix.
    """

    matrix = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        matrix[i][0] = i * gap

    for j in range(cols):
        matrix[0][j] = j * gap

    return matrix

def fill_matrix(matrix, seq1, seq2, match=1, mismatch=-1, gap=-1):
    """
    Fill the Needleman–Wunsch scoring matrix.
    """

    for i in range(1, len(seq1) + 1):
        for j in range(1, len(seq2) + 1):

            diagonal = (
                matrix[i - 1][j - 1]
                + score(seq1[i - 1], seq2[j - 1], match, mismatch)
            )

            up = matrix[i - 1][j] + gap

            left = matrix[i][j - 1] + gap

            matrix[i][j] = max(diagonal, up, left)

    return matrix

def traceback(
    matrix,
    seq1,
    seq2,
    match=1,
    mismatch=-1,
    gap=-1,
):
    """
    Trace back through the Needleman–Wunsch matrix
    to reconstruct the optimal alignment.
    """

    aligned1 = []
    aligned2 = []

    i = len(seq1)
    j = len(seq2)

    while i > 0 or j > 0:

        if (
            i > 0
            and j > 0
            and matrix[i][j]
            == matrix[i - 1][j - 1]
            + score(seq1[i - 1], seq2[j - 1], match, mismatch)
        ):

            aligned1.append(seq1[i - 1])
            aligned2.append(seq2[j - 1])

            i -= 1
            j -= 1

        elif i > 0 and matrix[i][j] == matrix[i - 1][j] + gap:

            aligned1.append(seq1[i - 1])
            aligned2.append("-")

            i -= 1

        else:

            aligned1.append("-")
            aligned2.append(seq2[j - 1])

            j -= 1

    return (
        "".join(reversed(aligned1)),
        "".join(reversed(aligned2)),
    )

def needleman_wunsch(
    seq1,
    seq2,
    match=1,
    mismatch=-1,
    gap=-1,
):
    """
    Perform global pairwise alignment using the
    Needleman–Wunsch algorithm.

    Parameters
    ----------
    seq1 : str
        First sequence.
    seq2 : str
        Second sequence.

    Returns
    -------
    tuple
        (aligned_seq1, aligned_seq2, score)
    """

    matrix = initialize_matrix(
        len(seq1) + 1,
        len(seq2) + 1,
        gap,
    )

    matrix = fill_matrix(
        matrix,
        seq1,
        seq2,
        match,
        mismatch,
        gap,
    )

    aligned1, aligned2 = traceback(
        matrix,
        seq1,
        seq2,
        match,
        mismatch,
        gap,
    )

    return (
        aligned1,
        aligned2,
        matrix[-1][-1],
    )

def alignment_statistics(aligned1, aligned2):
    """
    Calculate alignment statistics.
    """

    matches = 0
    mismatches = 0
    gaps = 0

    symbols = []

    for a, b in zip(aligned1, aligned2):

        if a == "-" or b == "-":
            gaps += 1
            symbols.append(" ")

        elif a == b:
            matches += 1
            symbols.append("|")

        else:
            mismatches += 1
            symbols.append(".")

    identity = (
        matches / len(aligned1) * 100
        if aligned1 else 0
    )

    return {
        "matches": matches,
        "mismatches": mismatches,
        "gaps": gaps,
        "identity": identity,
        "symbols": "".join(symbols),
        "length": len(aligned1),
    }

def consensus_sequence(aligned_sequences):
    """
    Generate a consensus sequence from aligned sequences.
    """

    if not aligned_sequences:
        return ""

    length = len(aligned_sequences[0])

    consensus = []

    for i in range(length):

        column = [
            sequence[i]
            for sequence in aligned_sequences
        ]

        counts = Counter(column)

        if "-" in counts:
            del counts["-"]

        if counts:
            consensus.append(
                counts.most_common(1)[0][0]
            )
        else:
            consensus.append("-")

    return "".join(consensus)

def format_alignment(sequence_names, aligned_sequences, consensus):
    """
    Format a multiple sequence alignment for display.
    """

    lines = []

    lines.append("=" * 70)
    lines.append("GenomeInsight Multiple Sequence Alignment")
    lines.append("=" * 70)
    lines.append("")

    width = max(len(name) for name in sequence_names) + 2

    for name, sequence in zip(sequence_names, aligned_sequences):
        lines.append(f"{name:<{width}}{sequence}")

    lines.append(f"{'Consensus':<{width}}{consensus}")

    return "\n".join(lines)

def progressive_alignment(sequences):
    """
    Perform a simple progressive multiple sequence alignment.

    Parameters
    ----------
    sequences : list
        List of DNA sequences.

    Returns
    -------
    dict
        Dictionary containing aligned sequences and consensus.
    """

    if len(sequences) < 2:
        raise ValueError(
            "At least two sequences are required."
        )

    aligned_sequences = []

    # Align first two sequences
    aligned1, aligned2, score = needleman_wunsch(
        sequences[0],
        sequences[1],
    )

    aligned_sequences.append(aligned1)
    aligned_sequences.append(aligned2)

    # Build consensus
    consensus = consensus_sequence(aligned_sequences)

    # Progressively align remaining sequences
    for sequence in sequences[2:]:

        consensus_aligned, aligned_sequence, score = needleman_wunsch(
            consensus,
            sequence,
        )

        aligned_sequences.append(aligned_sequence)

        consensus = consensus_sequence(aligned_sequences)

    return {
        "aligned_sequences": aligned_sequences,
        "consensus": consensus,
    }

def sequence_identity(seq1, seq2):
    """
    Calculate percentage identity between two aligned sequences.
    """

    if len(seq1) != len(seq2):
        raise ValueError(
            "Aligned sequences must have equal length."
        )

    matches = sum(
        a == b
        for a, b in zip(seq1, seq2)
    )

    return matches / len(seq1) * 100 if seq1 else 0

def identity_matrix(sequence_names, aligned_sequences):
    """
    Compute pairwise identity matrix.
    """

    matrix = []

    for seq1 in aligned_sequences:

        row = []

        for seq2 in aligned_sequences:

            row.append(
                round(
                    sequence_identity(seq1, seq2),
                    2,
                )
            )

        matrix.append(row)

    return matrix