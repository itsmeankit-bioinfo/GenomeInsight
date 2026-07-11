def reverse_complement(sequence: str) -> str:
    """
    Generate the reverse complement of a DNA sequence.

    Parameters
    ----------
    sequence : str
        DNA sequence.

    Returns
    -------
    str
        Reverse complement sequence.
    """

    sequence = sequence.upper()

    complement = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G",
        "N": "N"
    }

    reverse_seq = sequence[::-1]

    reverse_comp = ""

    for base in reverse_seq:
        reverse_comp += complement.get(base, "N")

    return reverse_comp