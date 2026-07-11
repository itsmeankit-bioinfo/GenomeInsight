from genomeinsight.analysis.orf import find_orfs


def register(subparsers):
    parser = subparsers.add_parser(
        "orf",
        help="Find open reading frames"
    )

    parser.add_argument(
        "sequence",
        help="DNA sequence"
    )

    parser.set_defaults(func=run)


def run(args):
    orfs = find_orfs(args.sequence)

    if not orfs:
        print("No ORFs found.")
        return

    print("\nGenomeInsight ORF Report")
    print("=" * 40)

    for index, orf in enumerate(orfs, start=1):

        print(f"\nORF {index}")
        print("-" * 20)

        print(f"Start  : {orf['start']}")
        print(f"End    : {orf['end']}")
        print(f"Length : {len(orf['sequence'])} bp")
        print(f"DNA    : {orf['sequence']}")