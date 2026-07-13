from genomeinsight.analysis.orf import find_orfs


def test_single_orf():
    orfs = find_orfs("ATGAAATAG")

    assert len(orfs) == 1
    assert orfs[0]["start"] == 1
    assert orfs[0]["end"] == 9
    assert orfs[0]["sequence"] == "ATGAAATAG"


def test_no_orf():
    assert find_orfs("AAAAAA") == []


def test_multiple_orfs():
    orfs = find_orfs("ATGAAATAGATGCCCTAA")
    assert len(orfs) == 2