def calculate_gc(sequence: str) -> float:
    """
    Calculate GC content of a DNA sequence.

    Parameters
    ----------
    sequence : str
        DNA sequence.

    Returns
    -------
    float
        GC percentage.
    """

    sequence = sequence.upper()

    if len(sequence) == 0:
        return 0.0

    gc_count = sequence.count("G") + sequence.count("C")

    return (gc_count / len(sequence)) * 100