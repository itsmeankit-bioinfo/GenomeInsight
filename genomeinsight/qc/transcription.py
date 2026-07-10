"""
DNA to RNA transcription utilities.
"""


def transcribe(sequence: str) -> str:
    """
    Convert a DNA sequence into RNA.
    """

    sequence = sequence.upper()

    return sequence.replace("T", "U")