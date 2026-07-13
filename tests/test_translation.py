from genomeinsight.analysis.translation import translate


def test_translation():
    assert translate("ATGGCC") == "MA"


def test_translation_stop():
    assert translate("ATGTAA") == "M*"


def test_translation_empty():
    assert translate("") == ""