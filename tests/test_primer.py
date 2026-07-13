from genomeinsight.analysis.primer import primer_analysis


def test_length():
    result = primer_analysis("ATGC")

    assert result["length"] == 4


def test_tm():
    result = primer_analysis("ATGC")

    assert result["tm"] == 12


def test_gc_clamp():
    result = primer_analysis("ATGC")

    assert result["gc_clamp"] is True