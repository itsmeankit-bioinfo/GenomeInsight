import argparse

from genomeinsight import __version__

from genomeinsight.commands import (
    align,
    fasta,
    fastq,
    fastqc,
    gc,
    gff,
    info,
    kmer,
    localalign,
    motif,
    n50,
    orf,
    primer,
    quality,
    restriction,
    reverse,
    stats,
    transcribe,
    translate,
    validate,
    protein,
)


def main():
    parser = argparse.ArgumentParser(
        prog="genomeinsight",
        description="GenomeInsight - A Python toolkit for genomics and metagenomics",
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"GenomeInsight v{__version__}",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        metavar="<command>",
        required=True,
    )

    # ==========================
    # General
    # ==========================
    info.register(subparsers)

    # ==========================
    # Sequence Analysis
    # ==========================
    gc.register(subparsers)
    reverse.register(subparsers)
    transcribe.register(subparsers)
    translate.register(subparsers)
    stats.register(subparsers)

    # ==========================
    # File Processing
    # ==========================
    fasta.register(subparsers)
    fastq.register(subparsers)
    validate.register(subparsers)
    gff.register(subparsers)

    # ==========================
    # Bioinformatics Algorithms
    # ==========================
    orf.register(subparsers)
    kmer.register(subparsers)
    motif.register(subparsers)
    restriction.register(subparsers)
    primer.register(subparsers)
    align.register(subparsers)
    localalign.register(subparsers)
    n50.register(subparsers)
    quality.register(subparsers)
    protein.register(subparsers)

    # ==========================
    # External Tools
    # ==========================
    fastqc.register(subparsers)

    # Future Integrations
    # fastp.register(subparsers)
    # bwa.register(subparsers)
    # samtools.register(subparsers)
    # spades.register(subparsers)
    # quast.register(subparsers)
    # prokka.register(subparsers)
    # blast.register(subparsers)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()