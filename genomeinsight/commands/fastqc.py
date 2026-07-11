from genomeinsight.tools.fastqc import run_fastqc


def register(subparsers):

    parser = subparsers.add_parser(
        "fastqc",
        help="Run FastQC quality analysis"
    )

    parser.add_argument(
        "file",
        help="FASTQ file"
    )

    parser.add_argument(
        "-o",
        "--output",
        default="fastqc_report",
        help="Output directory"
    )

    parser.set_defaults(func=run)


def run(args):

    print("Running FastQC...")

    output = run_fastqc(
        args.file,
        args.output
    )

    print(f"Report saved to: {output}")