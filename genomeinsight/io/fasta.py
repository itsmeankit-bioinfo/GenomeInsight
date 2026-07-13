"""
FASTA file parser for GenomeInsight.
"""


def read_fasta(file_path: str):
    """
    Read sequences from a FASTA file.

    Parameters
    ----------
    file_path : str
        Path to the FASTA file.

    Returns
    -------
    list
        List of dictionaries containing sequence IDs and sequences.
    """

    sequences = []

    current_id = None
    current_sequence = []

    with open(file_path, "r") as fasta_file:

        for line in fasta_file:

            line = line.strip()

            if not line:
                continue

            if line.startswith(">"):

                if current_id is not None:

                    sequences.append(
                        {
                            "id": current_id,
                            "sequence": "".join(current_sequence),
                        }
                    )

                current_id = line[1:]
                current_sequence = []

            else:
                current_sequence.append(line)

        if current_id is not None:

            sequences.append(
                {
                    "id": current_id,
                    "sequence": "".join(current_sequence),
                }
            )

    return sequences