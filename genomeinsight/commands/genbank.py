"""
GenBank CLI commands.
"""

from genomeinsight.io.genbank import (
    read_genbank,
    read_genes,
    read_cds,
)

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

def run_genes(args):
    """
    Display gene annotations.
    """

    genes = read_genes(args.file)

    print("=" * 60)
    print("Genes")
    print("=" * 60)

    if not genes:
        print("No gene annotations found.")
        return

    print(f"{'Gene':20}Location")
    print("-" * 60)

    for gene in genes:
        print(
            f"{gene['gene']:20}"
            f"{gene['location']}"
        )

def run_cds(args):
    """
    Display coding DNA sequences (CDS).
    """

    cds_list = read_cds(args.file)

    print("=" * 80)
    print("Coding DNA Sequences (CDS)")
    print("=" * 80)

    if not cds_list:
        print("No CDS annotations found.")
        return

    print(f"{'Gene':20}{'Product':35}Location")
    print("-" * 80)

    for cds in cds_list:
        print(
            f"{cds['gene']:20}"
            f"{cds['product'][:34]:35}"
            f"{cds['location']}"
        )


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

    genes_parser = genbank_subparsers.add_parser(
    "genes",
    help="Display gene annotations",
    )

    genes_parser.add_argument(
    "file",
    metavar="GENBANK",
    help="GenBank file",
    )

    genes_parser.set_defaults(func=run_genes)

    cds_parser = genbank_subparsers.add_parser(
    "cds",
    help="Display coding DNA sequences",
    )

    cds_parser.add_argument(
    "file",
    metavar="GENBANK",
    help="GenBank file",
    )

    cds_parser.set_defaults(func=run_cds)