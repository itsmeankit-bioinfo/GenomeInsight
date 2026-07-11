"""
K-mer counting utilities.
"""


def count_kmers(sequence: str, k: int):
    """
    Count k-mers in a DNA sequence.
    """

    sequence = sequence.upper()

    kmers = {}

    if k <= 0:
        return kmers

    for i in range(len(sequence) - k + 1):

        kmer = sequence[i:i + k]

        kmers[kmer] = kmers.get(kmer, 0) + 1

    return dict(sorted(kmers.items()))