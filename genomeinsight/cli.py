import argparse

from genomeinsight import __version__
from genomeinsight.qc.gc_content import calculate_gc
from genomeinsight.qc.reverse_complement import reverse_complement
from genomeinsight.qc.transcription import transcribe


def main():
    parser = argparse.ArgumentParser(
        prog="genomeinsight",
        description="GenomeInsight - A Python toolkit for genomics and metagenomics"
    )

    subparsers = parser.add_subparsers(dest="command")

    # ----------------------------
    # Version
    # ----------------------------
    subparsers.add_parser(
        "version",
        help="Show GenomeInsight version"
    )

    # ----------------------------
    # Info
    # ----------------------------
    subparsers.add_parser(
        "info",
        help="Display project information"
    )

    # ----------------------------
    # GC Content
    # ----------------------------
    gc_parser = subparsers.add_parser(
        "gc",
        help="Calculate GC content"
    )

    gc_parser.add_argument(
        "sequence",
        help="DNA sequence"
    )

    # ----------------------------
    # Reverse Complement
    # ----------------------------
    reverse_parser = subparsers.add_parser(
        "reverse",
        help="Generate reverse complement"
    )

    reverse_parser.add_argument(
        "sequence",
        help="DNA sequence"
    )

    # ----------------------------
    # DNA -> RNA
    # ----------------------------
    transcribe_parser = subparsers.add_parser(
        "transcribe",
        help="Transcribe DNA into RNA"
    )

    transcribe_parser.add_argument(
        "sequence",
        help="DNA sequence"
    )

    args = parser.parse_args()

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

    elif args.command == "reverse":
        rc = reverse_complement(args.sequence)

        print(f"Original Sequence           : {args.sequence.upper()}")
        print(f"Reverse Complement Sequence : {rc}")

    elif args.command == "transcribe":
        rna = transcribe(args.sequence)

        print(f"DNA Sequence : {args.sequence.upper()}")
        print(f"RNA Sequence : {rna}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()