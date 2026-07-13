"""
Protein analysis CLI command.
"""

from genomeinsight.analysis.protein import (
    analyze_protein,
    amino_acid_composition,
    molecular_weight,
)
from genomeinsight.io.fasta import read_fasta


def run_info(args):
    """
    Display summary statistics for protein sequences.
    """
    proteins = read_fasta(args.file)

    if not proteins:
        print("No protein sequences found.")
        return

    for protein in proteins:
        result = analyze_protein(protein["sequence"])

        print("=" * 60)
        print(f"Protein ID        : {protein['id']}")
        print(f"Length            : {result['length']} aa")
        print(f"Molecular Weight  : {result['molecular_weight']} Da")
        print(f"Isoelectric Point : {result['isoelectric_point']}")
        print(f"Aromaticity       : {result['aromaticity']}")
        print(f"Instability Index : {result['instability_index']}")
        print(f"GRAVY             : {result['gravy']}")


def run_composition(args):
    """
    Display amino acid composition.
    """
    proteins = read_fasta(args.file)

    if not proteins:
        print("No protein sequences found.")
        return

    for protein in proteins:
        composition = amino_acid_composition(protein["sequence"])

        print("=" * 60)
        print(f"Protein ID : {protein['id']}\n")

        for aa, count in sorted(composition.items()):
            print(f"{aa:2} : {count}")


def run_mw(args):
    """
    Display molecular weight.
    """
    proteins = read_fasta(args.file)

    if not proteins:
        print("No protein sequences found.")
        return

    for protein in proteins:
        mw = molecular_weight(protein["sequence"])

        print("=" * 60)
        print(f"Protein ID : {protein['id']}")
        print()
        print(f"Molecular Weight : {mw:.2f} Da")
        print(f"                 : {mw / 1000:.2f} kDa")


def register(subparsers):
    """
    Register protein commands.
    """

    protein_parser = subparsers.add_parser(
        "protein",
        help="Analyze protein sequences",
        description="Analyze protein sequences from FASTA files.",
    )

    protein_subparsers = protein_parser.add_subparsers(
        dest="protein_command",
        required=True,
    )

    # ------------------------------------------------------------
    # protein info
    # ------------------------------------------------------------
    info_parser = protein_subparsers.add_parser(
        "info",
        help="Display protein statistics",
        description=(
            "Display molecular weight, isoelectric point, "
            "GRAVY, aromaticity and instability index."
        ),
    )

    info_parser.add_argument(
        "file",
        metavar="FASTA",
        help="Path to a protein FASTA file",
    )

    info_parser.set_defaults(func=run_info)

    # ------------------------------------------------------------
    # protein composition
    # ------------------------------------------------------------
    composition_parser = protein_subparsers.add_parser(
        "composition",
        help="Display amino acid composition",
        description="Display amino acid composition of protein sequences.",
    )

    composition_parser.add_argument(
        "file",
        metavar="FASTA",
        help="Path to a protein FASTA file",
    )

    composition_parser.set_defaults(func=run_composition)

    # ------------------------------------------------------------
    # protein molecular weight
    # ------------------------------------------------------------
    mw_parser = protein_subparsers.add_parser(
        "mw",
        help="Calculate molecular weight",
        description="Calculate molecular weight of protein sequences.",
    )

    mw_parser.add_argument(
        "file",
        metavar="FASTA",
        help="Path to a protein FASTA file",
    )

    mw_parser.set_defaults(func=run_mw)