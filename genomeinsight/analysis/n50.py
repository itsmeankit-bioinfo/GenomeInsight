"""
Assembly statistics (N50/L50).
"""


def calculate_n50(lengths):
    """
    Calculate N50 and L50 from contig lengths.
    """

    if not lengths:
        return {
            "n50": 0,
            "l50": 0,
            "largest": 0,
            "total_length": 0,
            "total_contigs": 0,
        }

    lengths = sorted(lengths, reverse=True)

    total = sum(lengths)
    half = total / 2

    cumulative = 0

    for index, length in enumerate(lengths, start=1):

        cumulative += length

        if cumulative >= half:

            return {
                "n50": length,
                "l50": index,
                "largest": lengths[0],
                "total_length": total,
                "total_contigs": len(lengths),
            }