from genomeinsight.io.gff3 import read_gff3


def register(subparsers):

    parser = subparsers.add_parser(
        "gff",
        help="Read GFF3 annotation file"
    )

    parser.add_argument(
        "file",
        help="GFF3 file"
    )

    parser.set_defaults(func=run)


def run(args):

    features = read_gff3(args.file)

    print("\nGenomeInsight GFF3 Report")
    print("=" * 40)
    print()

    print(f"File            : {args.file}")
    print(f"Total Features  : {len(features)}")
    print()

    counts = {}

    for feature in features:
        counts[feature["type"]] = counts.get(feature["type"], 0) + 1

    for feature_type, count in sorted(counts.items()):
        print(f"{feature_type:<12}: {count}")