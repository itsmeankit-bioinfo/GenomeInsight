from genomeinsight.analysis.msa import(
    read_sequences,
    validate_sequences,
    initialize_matrix,
    fill_matrix,
    traceback,
    needleman_wunsch,
)

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import pytest

from genomeinsight.analysis.msa import (
    format_alignment,
    alignment_statistics,
    consensus_sequence,
)

def test_read_sequences():

    sequences = read_sequences("examples/msa.fasta")

    assert len(sequences) == 4
    assert sequences[0].id == "Human"
    assert str(sequences[0].seq) == "ATGGCTACGTAA"


def test_sequence_names():

    sequences = read_sequences("examples/msa.fasta")

    names = [seq.id for seq in sequences]

    assert names == [
        "Human",
        "Mouse",
        "Chimpanzee",
        "Dog",
    ]

def test_validate_sequences_success():

    sequences = read_sequences("examples/msa.fasta")

    validate_sequences(sequences)


def test_validate_minimum_sequences():

    sequences = [
        SeqRecord(Seq("ATGC"), id="Human")
    ]

    with pytest.raises(ValueError):
        validate_sequences(sequences)


def test_duplicate_ids():

    sequences = [
        SeqRecord(Seq("ATGC"), id="Human"),
        SeqRecord(Seq("ATGC"), id="Human"),
    ]

    with pytest.raises(ValueError):
        validate_sequences(sequences)


def test_invalid_nucleotide():

    sequences = [
        SeqRecord(Seq("ATGCX"), id="Human"),
        SeqRecord(Seq("ATGCA"), id="Mouse"),
    ]

    with pytest.raises(ValueError):
        validate_sequences(sequences)

def test_initialize_matrix():

    matrix = initialize_matrix(4, 5)

    assert matrix[0] == [0, -1, -2, -3, -4]
    assert matrix[1][0] == -1
    assert matrix[2][0] == -2
    assert matrix[3][0] == -3


def test_fill_matrix():

    matrix = initialize_matrix(3, 3)

    matrix = fill_matrix(
        matrix,
        "AT",
        "AT",
    )

    assert matrix[-1][-1] == 2

def test_traceback():

    matrix = initialize_matrix(3, 3)

    matrix = fill_matrix(
        matrix,
        "AT",
        "AT",
    )

    aligned1, aligned2 = traceback(
        matrix,
        "AT",
        "AT",
    )

    assert aligned1 == "AT"
    assert aligned2 == "AT"

def test_needleman_wunsch():

    aligned1, aligned2, score = needleman_wunsch(
        "AT",
        "AT",
    )

    assert aligned1 == "AT"
    assert aligned2 == "AT"
    assert score == 2

# Mismatch Test
def test_needleman_wunsch_mismatch():

    aligned1, aligned2, score = needleman_wunsch(
        "AT",
        "AG",
    )

    assert aligned1 == "AT"
    assert aligned2 == "AG"
    assert score == 0

# Gap Test
def test_needleman_wunsch_gap():

    aligned1, aligned2, score = needleman_wunsch(
        "ATG",
        "AG",
    )

    assert len(aligned1) == len(aligned2)
    assert "-" in aligned1 or "-" in aligned2

# Different length sequences Test
def test_needleman_wunsch_different_lengths():

    aligned1, aligned2, score = needleman_wunsch(
        "ATGC",
        "ATGCA",
    )

    assert len(aligned1) == len(aligned2)

# Empty sequence tests
def test_needleman_wunsch_empty():

    aligned1, aligned2, score = needleman_wunsch(
        "",
        "",
    )

    assert aligned1 == ""
    assert aligned2 == ""
    assert score == 0

def test_consensus_sequence():

    consensus = consensus_sequence(
        [
            "ATGCTAGC",
            "ATGTTAGC",
            "ATGCTAGC",
        ]
    )

    assert consensus == "ATGCTAGC"

def test_consensus_with_gaps():

    consensus = consensus_sequence(
        [
            "ATGC-AGC",
            "ATGCTAGC",
            "ATGC-AGC",
        ]
    )

    assert consensus == "ATGCTAGC"

def test_format_alignment():

    report = format_alignment(
        ["Human", "Mouse"],
        ["ATGC", "ATGT"],
        "ATGC",
    )

    assert "GenomeInsight Multiple Sequence Alignment" in report
    assert "Consensus" in report
    assert "Human" in report