from genomeinsight.analysis.gc_content import calculate_gc


def test_gc_100():
    assert calculate_gc("GGGG") == 100.0


def test_gc_0():
    assert calculate_gc("AAAA") == 0.0


def test_gc_50():
    assert calculate_gc("ATGC") == 50.0


def test_gc_empty():
    assert calculate_gc("") == 0.0