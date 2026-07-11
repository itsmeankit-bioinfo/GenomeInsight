from genomeinsight.analysis.restriction import find_restriction_sites


def register(subparsers):

    parser = subparsers.add_parser(
        "restriction",
        help="Find restriction enzyme sites"
    )

    parser.add_argument(
        "sequence",
        help="DNA sequence"
    )

    parser.set_defaults(func=run)


def run(args):

    sites = find_restriction_sites(args.sequence)

    print("\nGenomeInsight Restriction Site Report")
    print("=" * 45)

    if not sites:
        print("\nNo restriction sites found.")
        return

    print()

    for site in sites:

        print(
            f"{site['enzyme']:<10}"
            f"{site['site']:<12}"
            f"Position : {site['position']}"
        )