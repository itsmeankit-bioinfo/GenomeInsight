from genomeinsight.io.fasta import read_fasta
from genomeinsight.analysis.sequence_stats import sequence_statistics


def register(subparsers):
    parser = subparsers.add_parser(
        "fasta",
        help="Read and summarize a FASTA file"
    )

    parser.add_argument(
        "file",
        help="Path to FASTA file"
    )

    parser.set_defaults(func=run)


def run(args):
    sequences = read_fasta(args.file)

    print("\nGenomeInsight FASTA Report")
    print("=" * 40)
    print()

    print(f"File : {args.file}")
    print(f"Total Sequences : {len(sequences)}")

    for index, seq in enumerate(sequences, start=1):

        stats = sequence_statistics(seq["sequence"])

        print("\n" + "-" * 40)
        print(f"Sequence {index}")
        print("-" * 40)

        print(f"ID         : {seq['id']}")
        print(f"Length     : {stats['length']} bp")
        print(f"GC Content : {stats['gc_content']:.2f}%")