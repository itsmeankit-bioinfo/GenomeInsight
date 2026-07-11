from genomeinsight.analysis.motif import find_motif


def register(subparsers):
    parser = subparsers.add_parser(
        "motif",
        help="Find DNA motifs"
    )

    parser.add_argument(
        "sequence",
        help="DNA sequence"
    )

    parser.add_argument(
        "motif",
        help="DNA motif"
    )

    parser.set_defaults(func=run)


def run(args):

    positions = find_motif(
        args.sequence,
        args.motif
    )

    print("\nGenomeInsight Motif Report")
    print("=" * 40)

    print(f"\nMotif : {args.motif}")

    if positions:
        print(f"Occurrences : {len(positions)}")
        print("Positions   :", ", ".join(map(str, positions)))
    else:
        print("Motif not found.")