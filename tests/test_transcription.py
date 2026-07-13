from genomeinsight.analysis.transcription import transcribe


def test_transcription():
    assert transcribe("ATGC") == "AUGC"


def test_transcription_lowercase():
    assert transcribe("atgc") == "AUGC"


def test_transcription_empty():
    assert transcribe("") == ""