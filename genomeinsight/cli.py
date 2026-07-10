import argparse

from genomeinsight import __version__
from genomeinsight.qc.gc_content import calculate_gc


def main():
    parser = argparse.ArgumentParser(
        prog="genomeinsight",
        description="GenomeInsight - A Python toolkit for genomics and metagenomics"
    )

    subparsers = parser.add_subparsers(dest="command")

    # ----------------------------
    # Version Command
    # ----------------------------
    subparsers.add_parser(
        "version",
        help="Show GenomeInsight version"
    )

    # ----------------------------
    # Info Command
    # ----------------------------
    subparsers.add_parser(
        "info",
        help="Display project information"
    )

    # ----------------------------
    # GC Content Command
    # ----------------------------
    gc_parser = subparsers.add_parser(
        "gc",
        help="Calculate GC content of a DNA sequence"
    )

    gc_parser.add_argument(
        "sequence",
        help="DNA sequence"
    )

    args = parser.parse_args()

    # ----------------------------
    # Execute Commands
    # ----------------------------

    if args.command == "version":
        print(f"GenomeInsight v{__version__}")

    elif args.command == "info":
        print("GenomeInsight")
        print("Author : Ankit Raj")
        print("Python toolkit for genomics and metagenomics.")
        print()
        print("Available modules:")
        print(" - Quality Control")
        print(" - Assembly")
        print(" - Annotation")
        print(" - Metagenomics")

    elif args.command == "gc":
        gc = calculate_gc(args.sequence)

        gc_count = (
            args.sequence.upper().count("G")
            + args.sequence.upper().count("C")
        )

        print(f"Sequence Length : {len(args.sequence)}")
        print(f"GC Count        : {gc_count}")
        print(f"GC Content      : {gc:.2f}%")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()