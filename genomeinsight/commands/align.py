from genomeinsight.analysis.alignment import needleman_wunsch


def register(subparsers):

    parser = subparsers.add_parser(
        "align",
        help="Global sequence alignment"
    )

    parser.add_argument("sequence1")
    parser.add_argument("sequence2")

    parser.set_defaults(func=run)


def run(args):

    result = needleman_wunsch(
        args.sequence1,
        args.sequence2,
    )

    print("\nGenomeInsight Global Alignment")
    print("=" * 40)
    print()

    print(result["seq1"])
    print(result["seq2"])
    print()

    print(f"Alignment Score : {result['score']}")