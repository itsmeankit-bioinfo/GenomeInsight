"""
Protein analysis CLI command.
"""

from genomeinsight.analysis.protein import analyze_protein
from genomeinsight.io.fasta import read_fasta


def run_info(args):
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


def register(subparsers):
    protein_parser = subparsers.add_parser(
        "protein",
        help="Protein sequence analysis",
    )

    protein_subparsers = protein_parser.add_subparsers(
        dest="protein_command",
        required=True,
    )

    info_parser = protein_subparsers.add_parser(
        "info",
        help="Protein summary",
    )

    info_parser.add_argument(
        "file",
        help="Protein FASTA file",
    )

    info_parser.set_defaults(func=run_info)