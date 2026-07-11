from genomeinsight.analysis.sequence_stats import sequence_statistics


def register(subparsers):
    parser = subparsers.add_parser(
        "stats",
        help="Display sequence statistics"
    )

    parser.add_argument(
        "sequence",
        help="DNA sequence"
    )

    parser.set_defaults(func=run)


def run(args):
    stats = sequence_statistics(args.sequence)

    print("\nSequence Statistics")
    print("=" * 20)
    print()

    print(f"Sequence Length : {stats['length']}")
    print()

    print("Base Counts")
    print("-" * 11)

    print(f"A : {stats['A']}")
    print(f"T : {stats['T']}")
    print(f"G : {stats['G']}")
    print(f"C : {stats['C']}")
    print(f"N : {stats['N']}")
    print()

    print(f"GC Count : {stats['gc']}")
    print(f"AT Count : {stats['at']}")
    print()

    print(f"GC Content : {stats['gc_content']:.2f}%")
    print(f"AT Content : {stats['at_content']:.2f}%")