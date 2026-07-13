from genomeinsight.analysis.protein import analyze_protein


def test_length():

    result = analyze_protein("MKWVTF")

    assert result["length"] == 6


def test_molecular_weight():

    result = analyze_protein("MKWVTF")

    assert result["molecular_weight"] > 0


def test_pi():

    result = analyze_protein("MKWVTF")

    assert result["isoelectric_point"] > 0