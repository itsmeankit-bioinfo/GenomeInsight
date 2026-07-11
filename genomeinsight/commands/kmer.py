from genomeinsight.analysis.kmer import count_kmers


def register(subparsers):
    parser = subparsers.add_parser(
        "kmer",
        help="Count k-mers in a DNA sequence"
    )

    parser.add_argument(
        "sequence",
        help="DNA sequence"
    )

    parser.add_argument(
        "-k",
        "--kmer-size",
        type=int,
        required=True,
        help="K-mer size"
    )

    parser.set_defaults(func=run)


def run(args):
    kmers = count_kmers(args.sequence, args.kmer_size)

    print("\nGenomeInsight K-mer Report")
    print("=" * 40)
    print()

    print(f"K-mer Size : {args.kmer_size}\n")

    for kmer, count in kmers.items():
        print(f"{kmer} : {count}")