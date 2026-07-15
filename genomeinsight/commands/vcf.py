"""
VCF CLI commands for GenomeInsight.
"""

from genomeinsight.io.vcf import read_vcf
from genomeinsight.analysis.vcf import (
    variant_statistics, 
    extract_snps,
    extract_indels,
)


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

def run_snps(args):
    """
    Display SNP variants from a VCF file.
    """

    variants = read_vcf(args.file)
    snps = extract_snps(variants)

    print("=" * 60)
    print("SNP Variants")
    print("=" * 60)

    if not snps:
        print("No SNP variants found.")
        return

    print(f"{'Chrom':12}{'Position':12}{'REF':8}{'ALT'}")
    print("-" * 60)

    for snp in snps:
        print(
            f"{snp['chrom']:12}"
            f"{snp['pos']:12}"
            f"{snp['ref']:8}"
            f"{snp['alt']}"
        )

def run_indels(args):
    """
    Display insertion and deletion variants from a VCF file.
    """

    variants = read_vcf(args.file)
    indels = extract_indels(variants)

    print("=" * 70)
    print("INDEL Variants")
    print("=" * 70)

    if not indels:
        print("No INDEL variants found.")
        return

    print(f"{'Chrom':12}{'Position':12}{'REF':10}{'ALT':10}{'Type'}")
    print("-" * 70)

    for indel in indels:
        print(
            f"{indel['chrom']:12}"
            f"{indel['pos']:12}"
            f"{indel['ref']:10}"
            f"{indel['alt']:10}"
            f"{indel['type']}"
        )

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

    snps_parser = vcf_subparsers.add_parser(
        "snps",
        help="Display SNP variants",
    )

    snps_parser.add_argument(
        "file",
        metavar="VCF",
        help="VCF file",
    )

    snps_parser.set_defaults(func=run_snps)

    indels_parser = vcf_subparsers.add_parser(
        "indels",
        help="Display insertion and deletion variants",
    )

    indels_parser.add_argument(
        "file",
        metavar="VCF",
        help="VCF file",
    )

    indels_parser.set_defaults(func=run_indels)