from genomeinsight.io.fastq import read_fastq
from genomeinsight.analysis.quality import quality_statistics


def register(subparsers):

    parser = subparsers.add_parser(
        "quality",
        help="FASTQ quality statistics"
    )

    parser.add_argument(
        "file",
        help="FASTQ file"
    )

    parser.set_defaults(func=run)


def run(args):

    reads = read_fastq(args.file)

    stats = quality_statistics(reads)

    print("\nGenomeInsight FASTQ Quality Report")
    print("=" * 40)
    print()

    print(f"File              : {args.file}")
    print(f"Average Quality   : {stats['average']:.2f}")
    print(f"Minimum Quality   : {stats['minimum']}")
    print(f"Maximum Quality   : {stats['maximum']}")
    print()
    print(f"Q20 Bases         : {stats['q20']}")
    print(f"Q30 Bases         : {stats['q30']}")
    print()
    print(f"Q20 Percentage    : {stats['q20_percent']:.2f}%")
    print(f"Q30 Percentage    : {stats['q30_percent']:.2f}%")