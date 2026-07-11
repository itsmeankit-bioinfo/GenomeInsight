from genomeinsight.io.fasta import read_fasta
from genomeinsight.analysis.n50 import calculate_n50


def register(subparsers):

    parser = subparsers.add_parser(
        "n50",
        help="Calculate assembly N50"
    )

    parser.add_argument(
        "file",
        help="Assembly FASTA"
    )

    parser.set_defaults(func=run)


def run(args):

    sequences = read_fasta(args.file)

    lengths = [
        len(seq["sequence"])
        for seq in sequences
    ]

    stats = calculate_n50(lengths)

    print("\nGenomeInsight Assembly Report")
    print("=" * 40)
    print()

    print(f"Total Contigs : {stats['total_contigs']}")
    print(f"Total Length  : {stats['total_length']} bp")
    print(f"Largest Contig: {stats['largest']} bp")
    print()
    print(f"N50           : {stats['n50']} bp")
    print(f"L50           : {stats['l50']}")