from genomeinsight.analysis.gc_content import calculate_gc


def register(subparsers):
    parser = subparsers.add_parser(
        "gc",
        help="Calculate GC content"
    )

    parser.add_argument(
        "sequence",
        help="DNA sequence"
    )

    parser.set_defaults(func=run)


def run(args):
    gc = calculate_gc(args.sequence)

    gc_count = (
        args.sequence.upper().count("G")
        + args.sequence.upper().count("C")
    )

    print(f"Sequence Length : {len(args.sequence)}")
    print(f"GC Count        : {gc_count}")
    print(f"GC Content      : {gc:.2f}%")