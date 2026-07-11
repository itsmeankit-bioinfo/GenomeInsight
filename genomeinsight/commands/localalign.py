from genomeinsight.analysis.local_alignment import smith_waterman


def register(subparsers):

    parser = subparsers.add_parser(
        "localalign",
        help="Smith-Waterman local alignment"
    )

    parser.add_argument("sequence1")
    parser.add_argument("sequence2")

    parser.set_defaults(func=run)


def run(args):

    result = smith_waterman(
        args.sequence1,
        args.sequence2
    )

    print("\nGenomeInsight Local Alignment")
    print("=" * 40)
    print()

    print(result["seq1"])
    print(result["seq2"])
    print()

    print(f"Alignment Score : {result['score']}")