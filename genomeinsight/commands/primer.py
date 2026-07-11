from genomeinsight.analysis.primer import primer_analysis


def register(subparsers):

    parser = subparsers.add_parser(
        "primer",
        help="Analyze PCR primer"
    )

    parser.add_argument(
        "sequence",
        help="Primer sequence"
    )

    parser.set_defaults(func=run)


def run(args):

    result = primer_analysis(args.sequence)

    print("\nGenomeInsight Primer Report")
    print("=" * 40)
    print()

    print(f"Sequence    : {args.sequence.upper()}")
    print(f"Length      : {result['length']} bp")
    print(f"GC Content  : {result['gc']:.2f}%")
    print(f"AT Content  : {result['at']:.2f}%")
    print(f"Tm          : {result['tm']} °C")
    print(
        f"GC Clamp    : {'Yes' if result['gc_clamp'] else 'No'}"
    )