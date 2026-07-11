"""
FASTQ statistics utilities.
"""


def fastq_statistics(reads):
    """
    Calculate basic FASTQ statistics.
    """

    if not reads:
        return {
            "total_reads": 0,
            "average_length": 0,
            "minimum_length": 0,
            "maximum_length": 0,
            "gc_content": 0,
            "average_quality": 0,
        }

    lengths = []
    gc_count = 0
    total_bases = 0
    quality_scores = []

    for read in reads:
        sequence = read["sequence"].upper()
        quality = read["quality"]

        length = len(sequence)
        lengths.append(length)

        total_bases += length
        gc_count += sequence.count("G") + sequence.count("C")

        for char in quality:
            # Phred+33 encoding
            quality_scores.append(ord(char) - 33)

    return {
        "total_reads": len(reads),
        "average_length": sum(lengths) / len(lengths),
        "minimum_length": min(lengths),
        "maximum_length": max(lengths),
        "gc_content": (gc_count / total_bases) * 100 if total_bases else 0,
        "average_quality": (
            sum(quality_scores) / len(quality_scores)
            if quality_scores else 0
        ),
    }