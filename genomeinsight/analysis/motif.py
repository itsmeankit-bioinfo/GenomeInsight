"""
Motif searching utilities.
"""


def find_motif(sequence: str, motif: str):
    """
    Find all occurrences of a motif in a DNA sequence.
    """

    sequence = sequence.upper()
    motif = motif.upper()

    positions = []

    start = 0

    while True:
        index = sequence.find(motif, start)

        if index == -1:
            break

        positions.append(index + 1)

        start = index + 1

    return positions