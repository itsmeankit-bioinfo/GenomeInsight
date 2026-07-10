import argparse

from genomeinsight import __version__


def main():
    parser = argparse.ArgumentParser(
        prog="genomeinsight",
        description="GenomeInsight - A Python toolkit for genomics and metagenomics"
    )

    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser(
        "version",
        help="Show GenomeInsight version"
    )

    subparsers.add_parser(
        "info",
        help="Display project information"
    )

    args = parser.parse_args()

    if args.command == "version":
        print(f"GenomeInsight v{__version__}")

    elif args.command == "info":
        print("GenomeInsight")
        print("Author : Ankit Raj")
        print("Python toolkit for genomics and metagenomics.")
        print()
        print("Available modules")
        print(" - Quality Control")
        print(" - Assembly")
        print(" - Annotation")
        print(" - Metagenomics")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()