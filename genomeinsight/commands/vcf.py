"""
VCF CLI commands for GenomeInsight.
"""
from genomeinsight.io.export import ( 
    export_csv,
    export_json,
)

from genomeinsight.io.vcf import read_vcf
from genomeinsight.analysis.vcf import (
    variant_statistics, 
    extract_snps,
    extract_indels,
    chromosome_statistics,
    generate_summary,
    transition_transversion_ratio,
    filter_variants,
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

def run_chromosomes(args):
    """
    Display chromosome statistics from a VCF file.
    """

    variants = read_vcf(args.file)
    chromosomes = chromosome_statistics(variants)

    print("=" * 60)
    print("Chromosome Statistics")
    print("=" * 60)

    if not chromosomes:
        print("No variants found.")
        return

    print(f"{'Chromosome':20}Variants")
    print("-" * 60)

    for chrom, count in sorted(chromosomes.items()):
        print(f"{chrom:20}{count}")

def run_summary(args):
    """
    Display a complete VCF summary.
    """

    variants = read_vcf(args.file)
    summary = generate_summary(variants)

    stats = summary["statistics"]
    chromosomes = summary["chromosomes"]

    print("=" * 60)
    print("VCF Summary")
    print("=" * 60)

    print("\nGeneral Statistics")
    print("-" * 60)
    print(f"Total Variants : {stats['variants']}")
    print(f"Chromosomes    : {stats['chromosomes']}")
    print(f"SNPs           : {stats['snps']}")
    print(f"Insertions     : {stats['insertions']}")
    print(f"Deletions      : {stats['deletions']}")

    print("\nVariants by Chromosome")
    print("-" * 60)

    for chrom, count in sorted(chromosomes.items()):
        print(f"{chrom:15}: {count}")

def run_tstv(args):
    """
    Display transition/transversion statistics.
    """

    variants = read_vcf(args.file)
    stats = transition_transversion_ratio(variants)

    print("=" * 60)
    print("Transition / Transversion Statistics")
    print("=" * 60)

    print(f"Transitions     : {stats['transitions']}")
    print(f"Transversions   : {stats['transversions']}")

    print()

    if stats["ratio"] is None:
        print("Ts/Tv Ratio     : Undefined")
    else:
        print(f"Ts/Tv Ratio     : {stats['ratio']:.2f}")

def run_filter(args):
    """
    Filter variants by chromosome and/or type.
    """

    variants = read_vcf(args.file)

    filtered = filter_variants(
        variants,
        chromosome=args.chrom,
        variant_type=args.type,
    )

    print("=" * 70)
    print("Filtered Variants")
    print("=" * 70)

    if not filtered:
        print("No variants matched the filter.")
        return

    print(f"{'Chrom':12}{'Position':12}{'REF':8}{'ALT'}")
    print("-" * 70)

    for variant in filtered:
        print(
            f"{variant['chrom']:12}"
            f"{variant['pos']:12}"
            f"{variant['ref']:8}"
            f"{variant['alt']}"
        )

def run_export(args):
    """
    Export variants to supported formats.
    """

    variants = read_vcf(args.file)

    output = args.output

    if output is None:
        output = f"variants.{args.format}"

    if args.format == "csv":
        export_csv(variants, output)

    elif args.format == "json":
        export_json(variants, output)

    print()
    print("✓ Export completed successfully")
    print(f"Saved to: {output}")

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

    chromosomes_parser = vcf_subparsers.add_parser(
        "chromosomes",
        help="Display chromosome statistics",
    )

    chromosomes_parser.add_argument(
        "file",
        metavar="VCF",
        help="VCF file",
    )

    chromosomes_parser.set_defaults(func=run_chromosomes)


    summary_parser = vcf_subparsers.add_parser(
        "summary",
        help="Display a complete VCF summary",
    )

    summary_parser.add_argument(
        "file",
        metavar="VCF",
        help="VCF file",
    )

    summary_parser.set_defaults(func=run_summary)
    
    tstv_parser = vcf_subparsers.add_parser(
        "tstv",
        help="Calculate transition/transversion ratio",
    )

    tstv_parser.add_argument(
        "file",
        metavar="VCF",
        help="VCF file",
    )

    tstv_parser.set_defaults(func=run_tstv)

    filter_parser = vcf_subparsers.add_parser(
    "filter",
    help="Filter VCF variants",
    )

    filter_parser.add_argument(
        "file",
        metavar="VCF",
        help="VCF file",
    )

    filter_parser.add_argument(
        "--chrom",
        help="Filter by chromosome",
    )

    filter_parser.add_argument(
        "--type",
        choices=["snp", "indel"],
        help="Filter by variant type",
    )

    filter_parser.set_defaults(func=run_filter)

    export_parser = vcf_subparsers.add_parser(
        "export",
        help="Export variants",
    )

    export_parser.add_argument(
        "file",
        metavar="VCF",
        help="VCF file",
    )

    export_parser.add_argument(
        "--format",
        choices=["csv", "json"],
        required=True,
        help="Export format",
    )

    export_parser.add_argument(
        "--output",
        help="Output filename",
    )

    export_parser.set_defaults(func=run_export)