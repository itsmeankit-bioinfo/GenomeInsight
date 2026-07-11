import argparse

from genomeinsight import __version__

from genomeinsight.commands import (
    info,
    gc,
    reverse,
    transcribe,
    translate,
    stats,
    fasta,
    fastq,
    orf,
    kmer,
    motif,
    restriction,
    primer,
    n50,
    quality,
    gff,
    align,
    localalign,
)


def main():
    parser = argparse.ArgumentParser(
        prog="genomeinsight",
        description="GenomeInsight - A Python toolkit for genomics and metagenomics"
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"GenomeInsight v{__version__}"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        metavar="<command>"
    )

    # Register commands
    info.register(subparsers)
    gc.register(subparsers)
    reverse.register(subparsers)
    transcribe.register(subparsers)
    translate.register(subparsers)
    stats.register(subparsers)
    fasta.register(subparsers)
    fastq.register(subparsers)
    orf.register(subparsers)
    kmer.register(subparsers)
    motif.register(subparsers)
    restriction.register(subparsers)
    primer.register(subparsers)
    n50.register(subparsers)
    quality.register(subparsers)
    gff.register(subparsers)
    align.register(subparsers)
    localalign.register(subparsers)
    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()