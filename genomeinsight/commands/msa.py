"""
CLI commands for Multiple Sequence Alignment.
"""

from genomeinsight.analysis.msa import (
    read_sequences,
    validate_sequences,
    needleman_wunsch,
    alignment_statistics,
    progressive_alignment,
    format_alignment,
)


def run_pairwise(args):
    """
    Run pairwise Needleman–Wunsch alignment.
    """

    sequences = read_sequences(args.file)

    validate_sequences(sequences)

    if len(sequences) == 2:

        seq1 = str(sequences[0].seq)
        seq2 = str(sequences[1].seq)

        aligned1, aligned2, score = needleman_wunsch(
        seq1,
        seq2,
    )

        stats = alignment_statistics(
        aligned1,
        aligned2,
    )

        print()
        print("=" * 60)
        print("GenomeInsight Pairwise Alignment")
        print("=" * 60)
        print()

        print(f"Sequence 1 : {sequences[0].id}")
        print(f"Sequence 2 : {sequences[1].id}")
        print()

        print(f"{sequences[0].id:<10} {aligned1}")
        print(f"{'':<10} {stats['symbols']}")
        print(f"{sequences[1].id:<10} {aligned2}")

        print()

        print(f"Alignment Score : {score}")
        print(f"Identity        : {stats['identity']:.2f}%")
        print(f"Matches         : {stats['matches']}")
        print(f"Mismatches      : {stats['mismatches']}")
        print(f"Gaps            : {stats['gaps']}")
        print(f"Length          : {stats['length']}")

    else:

        names = [
            seq.id
            for seq in sequences
    ]

    dna = [
        str(seq.seq)
        for seq in sequences
    ]

    result = progressive_alignment(
        dna
    )

    report = format_alignment(
        names,
        result["aligned_sequences"],
        result["consensus"],
    )

    print(report)

def register(subparsers):
    parser = subparsers.add_parser(
        "msa",
        help="Multiple Sequence Alignment",
    )

    parser.add_argument(
        "file",
        help="Input FASTA file",
    )

    parser.set_defaults(func=run_pairwise)