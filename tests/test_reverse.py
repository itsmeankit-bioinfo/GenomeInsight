from genomeinsight.analysis.reverse_complement import reverse_complement


def test_reverse_complement():
    assert reverse_complement("ATGC") == "GCAT"


def test_reverse_lowercase():
    assert reverse_complement("atgc") == "GCAT"


def test_reverse_empty():
    assert reverse_complement("") == ""