"""
GenBank CLI commands.
"""

from genomeinsight.io.genbank import (
    read_genbank,
    read_genes,
    read_cds,
    read_proteins,
    read_features,
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

def run_proteins(args):
    """
    Display protein annotations from a GenBank file.
    """

    proteins = read_proteins(args.file)

    print("=" * 90)
    print("Proteins")
    print("=" * 90)

    if not proteins:
        print("No protein annotations found.")
        return

    print(f"{'Gene':20}{'Protein ID':25}Product")
    print("-" * 90)

    for protein in proteins:
        print(
            f"{protein['gene']:20}"
            f"{protein['protein_id']:25}"
            f"{protein['product']}"
        )

def run_features(args):
    """
    Display feature summary from a GenBank file.
    """

    features = read_features(args.file)

    print("=" * 60)
    print("GenBank Feature Summary")
    print("=" * 60)

    print(f"{'Feature Type':25}Count")
    print("-" * 60)

    for feature, count in sorted(features.items()):
        print(f"{feature:25}{count}")

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

    proteins_parser = genbank_subparsers.add_parser(
        "proteins",
        help="Display protein annotations",
    )

    proteins_parser.add_argument(
        "file",
        metavar="GENBANK",
        help="GenBank file",
    )

    proteins_parser.set_defaults(func=run_proteins)

    features_parser = genbank_subparsers.add_parser(
        "features",
        help="Display GenBank feature summary",
    )

    features_parser.add_argument(
        "file",
        metavar="GENBANK",
        help="GenBank file",
    )

    features_parser.set_defaults(func=run_features)