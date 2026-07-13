from genomeinsight.analysis.motif import find_motif


def test_positions():
    assert find_motif(
        "ATGCATGC",
        "ATG"
    ) == [1, 5]


def test_not_found():
    assert find_motif(
        "AAAA",
        "TT"
    ) == []


def test_overlap():
    assert find_motif(
        "AAAAA",
        "AA"
    ) == [1, 2, 3, 4]