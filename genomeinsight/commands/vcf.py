"""
VCF CLI commands for GenomeInsight.
"""

from genomeinsight.io.vcf import read_vcf
from genomeinsight.analysis.vcf import variant_statistics


def run_stats(args):
    """
    Display VCF statistics.
    """

    variants = read_vcf(args.file)
    stats = variant_statistics(variants)

    print("=" * 60)
    print("VCF Statistics")
    print("=" * 60)
    print(f"Total Variants : {stats['variants']}")
    print(f"Chromosomes    : {stats['chromosomes']}")
    print(f"SNPs           : {stats['snps']}")
    print(f"Insertions     : {stats['insertions']}")
    print(f"Deletions      : {stats['deletions']}")


def register(subparsers):
    """
    Register VCF commands.
    """

    parser = subparsers.add_parser(
        "vcf",
        help="Variant Call Format (VCF) tools",
    )

    vcf_subparsers = parser.add_subparsers(
        dest="vcf_command",
        required=True,
    )

    stats_parser = vcf_subparsers.add_parser(
        "stats",
        help="Display VCF statistics",
    )

    stats_parser.add_argument(
        "file",
        metavar="VCF",
        help="VCF file",
    )

    stats_parser.set_defaults(func=run_stats)