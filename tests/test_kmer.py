from genomeinsight.analysis.kmer import count_kmers


def test_kmer():
    assert count_kmers("ATAT", 2) == {
        "AT": 2,
        "TA": 1,
    }


def test_k1():
    assert count_kmers("AAA", 1) == {
        "A": 3,
    }


def test_invalid():
    assert count_kmers("ATGC", 0) == {}