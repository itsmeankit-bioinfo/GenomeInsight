def register(subparsers):
    parser = subparsers.add_parser(
        "info",
        help="Display project information"
    )

    parser.set_defaults(func=run)


def run(args):
    print("GenomeInsight")
    print("Author : Ankit Raj")
    print("Python toolkit for genomics and metagenomics.")
    print()
    print("Available modules:")
    print(" - Analysis")
    print(" - Assembly")
    print(" - Annotation")
    print(" - Metagenomics")