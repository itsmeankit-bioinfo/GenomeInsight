"""
HTML report command for GenomeInsight.
"""

from pathlib import Path

from genomeinsight.analysis.vcf import generate_summary
from genomeinsight.io.vcf import read_vcf
from genomeinsight.reports.html import create_html_report


def run_report(args):
    """
    Generate an HTML report from a VCF file.
    """

    variants = read_vcf(args.file)
    summary = generate_summary(variants)

    stats = summary["statistics"]
    chromosomes = summary["chromosomes"]

    chromosome_rows = ""

    for chrom, count in sorted(chromosomes.items()):
        chromosome_rows += (
            f"<tr><td>{chrom}</td><td>{count}</td></tr>"
        )

    body = f"""
<h2>General Statistics</h2>

<table>

<tr><th>Metric</th><th>Value</th></tr>

<tr><td>Total Variants</td><td>{stats['variants']}</td></tr>

<tr><td>Chromosomes</td><td>{stats['chromosomes']}</td></tr>

<tr><td>SNPs</td><td>{stats['snps']}</td></tr>

<tr><td>Insertions</td><td>{stats['insertions']}</td></tr>

<tr><td>Deletions</td><td>{stats['deletions']}</td></tr>

</table>

<br>

<h2>Variants by Chromosome</h2>

<table>

<tr><th>Chromosome</th><th>Variants</th></tr>

{chromosome_rows}

</table>
"""

    html = create_html_report(
        "GenomeInsight VCF Report",
        body,
    )

    output = Path("report.html")

    output.write_text(
        html,
        encoding="utf-8",
    )

    print("✓ HTML report generated successfully")
    print(f"Saved to: {output}")

def register(subparsers):
    """
    Register report commands.
    """

    parser = subparsers.add_parser(
        "report",
        help="Generate HTML reports",
    )

    parser.add_argument(
        "file",
        metavar="INPUT",
        help="Input VCF file",
    )

    parser.set_defaults(func=run_report)