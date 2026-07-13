"""
Protein analysis command.
"""

from genomeinsight.analysis.protein import protein_info
from genomeinsight.io.fasta import read_fasta


def run_protein(args):
    """
    Run protein analysis on a FASTA file.
    """

    proteins = read_fasta(args.file)

    if not proteins:
        print("No protein sequences found.")
        return

    for protein in proteins:
        result = protein_info(protein["sequence"])

        print("=" * 60)
        print(f"Protein ID        : {protein['id']}")
        print(f"Length            : {result['length']} aa")
        print(f"Molecular Weight  : {result['molecular_weight']} Da")
        print(f"Isoelectric Point : {result['isoelectric_point']}")
        print(f"Aromaticity       : {result['aromaticity']}")
        print(f"Instability Index : {result['instability_index']}")
        print(f"GRAVY             : {result['gravy']}")


def register(subparsers):
    """
    Register the protein command.
    """

    parser = subparsers.add_parser(
        "protein",
        help="Analyze protein sequences from a FASTA file",
    )

    parser.add_argument(
        "file",
        help="Protein FASTA file",
    )

    parser.set_defaults(func=run_protein)