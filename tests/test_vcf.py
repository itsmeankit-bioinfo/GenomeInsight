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

VCF_FILE = "examples/sample.vcf"


def test_read_vcf():
    variants = read_vcf(VCF_FILE)

    assert isinstance(variants, list)
    assert len(variants) > 0


def test_variant_keys():
    variants = read_vcf(VCF_FILE)

    variant = variants[0]

    assert "chrom" in variant
    assert "pos" in variant
    assert "ref" in variant
    assert "alt" in variant

def test_variant_statistics():
    variants = read_vcf(VCF_FILE)

    stats = variant_statistics(variants)

    assert stats["variants"] == 5
    assert stats["chromosomes"] == 2
    assert stats["snps"] == 3
    assert stats["insertions"] == 1
    assert stats["deletions"] == 1

def test_extract_snps():
    variants = read_vcf(VCF_FILE)

    snps = extract_snps(variants)

    assert len(snps) == 3

    for variant in snps:
        assert len(variant["ref"]) == 1
        assert len(variant["alt"]) == 1

def test_extract_indels():
    variants = read_vcf(VCF_FILE)

    indels = extract_indels(variants)

    assert len(indels) == 2

    for variant in indels:
        assert len(variant["ref"]) != len(variant["alt"])

def test_chromosome_statistics():
    variants = read_vcf(VCF_FILE)

    stats = chromosome_statistics(variants)

    assert stats["chr1"] == 4
    assert stats["chr2"] == 1

def test_generate_summary():
    variants = read_vcf(VCF_FILE)

    summary = generate_summary(variants)

    assert "statistics" in summary
    assert "chromosomes" in summary

    assert summary["statistics"]["variants"] == 5

def test_transition_transversion_ratio():
    variants = read_vcf(VCF_FILE)

    stats = transition_transversion_ratio(variants)

    assert stats["transitions"] == 3
    assert stats["transversions"] == 0
    assert stats["ratio"] is None

def test_filter_by_chromosome():
    variants = read_vcf(VCF_FILE)

    filtered = filter_variants(
        variants,
        chromosome="chr1",
    )

    assert len(filtered) == 4

def test_filter_snps():
    variants = read_vcf(VCF_FILE)

    filtered = filter_variants(
        variants,
        variant_type="snp",
    )

    assert len(filtered) == 3

def test_filter_indels():
    variants = read_vcf(VCF_FILE)

    filtered = filter_variants(
        variants,
        variant_type="indel",
    )

    assert len(filtered) == 2

