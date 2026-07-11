from genomeinsight.analysis.translation import translate


def register(subparsers):
    parser = subparsers.add_parser(
        "translate",
        help="Translate DNA into protein"
    )

    parser.add_argument(
        "sequence",
        help="DNA sequence"
    )

    parser.set_defaults(func=run)


def run(args):
    protein = translate(args.sequence)

    print(f"DNA Sequence     : {args.sequence.upper()}")
    print(f"Protein Sequence : {protein}")