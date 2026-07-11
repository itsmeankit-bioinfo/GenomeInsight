from genomeinsight.analysis.reverse_complement import reverse_complement


def register(subparsers):
    parser = subparsers.add_parser(
        "reverse",
        help="Generate reverse complement"
    )

    parser.add_argument(
        "sequence",
        help="DNA sequence"
    )

    parser.set_defaults(func=run)


def run(args):
    rc = reverse_complement(args.sequence)

    print(f"Original Sequence           : {args.sequence.upper()}")
    print(f"Reverse Complement Sequence : {rc}")