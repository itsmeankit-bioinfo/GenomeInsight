"""
GenBank CLI commands.
"""

from genomeinsight.io.genbank import read_genbank


def run_info(args):
    """
    Display GenBank file information.
    """

    info = read_genbank(args.file)

    print("=" * 60)
    print("GenBank Information")
    print("=" * 60)

    print(f"ID            : {info['id']}")
    print(f"Name          : {info['name']}")
    print(f"Description   : {info['description']}")
    print(f"Organism      : {info['organism']}")
    print(f"Length        : {info['length']} bp")
    print(f"Molecule Type : {info['molecule_type']}")
    print(f"Topology      : {info['topology']}")


def register(subparsers):
    """
    Register GenBank commands.
    """

    parser = subparsers.add_parser(
        "genbank",
        help="GenBank file utilities",
    )

    genbank_subparsers = parser.add_subparsers(
        dest="genbank_command",
    )

    info_parser = genbank_subparsers.add_parser(
        "info",
        help="Display GenBank information",
    )

    info_parser.add_argument(
        "file",
        metavar="GENBANK",
        help="GenBank file",
    )

    info_parser.set_defaults(func=run_info)