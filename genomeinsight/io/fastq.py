"""
FASTQ file parser for GenomeInsight.
"""


def read_fastq(file_path: str):
    """
    Read sequences from a FASTQ file.

    Parameters
    ----------
    file_path : str
        Path to FASTQ file.

    Returns
    -------
    list
        List of reads.
    """

    reads = []

    with open(file_path, "r") as file:

        while True:

            header = file.readline().strip()

            if not header:
                break

            sequence = file.readline().strip()
            plus = file.readline().strip()
            quality = file.readline().strip()

            reads.append({
                "id": header[1:],
                "sequence": sequence,
                "quality": quality
            })

    return reads