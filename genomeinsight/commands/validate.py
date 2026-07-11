from genomeinsight.io.fasta import read_fasta
from genomeinsight.io.validator import validate_fasta


def register(subparsers):
    parser = subparsers.add_parser(
        "validate",
        help="Validate a FASTA file"
    )

    parser.add_argument(
        "file",
        help="Path to FASTA file"
    )

    parser.set_defaults(func=run)


def run(args):
    sequences = read_fasta(args.file)
    report = validate_fasta(sequences)

    print("\nGenomeInsight FASTA Validation")
    print("=" * 40)
    print()

    for result in report:

        if result["valid"]:
            print(f"✓ {result['id']} : Valid")

        else:
            print(f"\n✗ {result['id']}")

            for error in result["errors"]:
                print(f"  - {error}")