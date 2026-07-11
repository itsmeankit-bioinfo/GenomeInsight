from genomeinsight.io.fastq import read_fastq
from genomeinsight.analysis.fastq_stats import fastq_statistics


def register(subparsers):
    parser = subparsers.add_parser(
        "fastq",
        help="Read and summarize a FASTQ file"
    )

    parser.add_argument(
        "file",
        help="Path to FASTQ file"
    )

    parser.set_defaults(func=run)


def run(args):
    reads = read_fastq(args.file)

    stats = fastq_statistics(reads)

    print("\nGenomeInsight FASTQ Report")
    print("=" * 40)
    print()

    print(f"File             : {args.file}")
    print(f"Total Reads      : {stats['total_reads']}")
    print(f"Average Length   : {stats['average_length']:.2f} bp")
    print(f"Minimum Length   : {stats['minimum_length']} bp")
    print(f"Maximum Length   : {stats['maximum_length']} bp")
    print(f"GC Content       : {stats['gc_content']:.2f}%")
    print(f"Average Quality  : {stats['average_quality']:.2f}")