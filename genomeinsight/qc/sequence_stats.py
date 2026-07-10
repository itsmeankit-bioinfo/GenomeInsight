"""
Sequence statistics utilities.
"""


def sequence_statistics(sequence: str) -> dict:
    """
    Generate basic statistics for a DNA sequence.
    """

    sequence = sequence.upper()

    length = len(sequence)

    a = sequence.count("A")
    t = sequence.count("T")
    g = sequence.count("G")
    c = sequence.count("C")
    n = sequence.count("N")

    gc = g + c
    at = a + t

    gc_content = (gc / length * 100) if length else 0
    at_content = (at / length * 100) if length else 0

    return {
        "length": length,
        "A": a,
        "T": t,
        "G": g,
        "C": c,
        "N": n,
        "gc": gc,
        "at": at,
        "gc_content": gc_content,
        "at_content": at_content,
    }