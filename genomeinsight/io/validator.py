"""
FASTA validation utilities.
"""

VALID_BASES = {"A", "T", "G", "C", "N"}


def validate_fasta(sequences):
    """
    Validate parsed FASTA sequences.

    Parameters
    ----------
    sequences : list
        Output from read_fasta().

    Returns
    -------
    list
        Validation report.
    """

    report = []

    ids = set()

    for seq in sequences:

        errors = []

        seq_id = seq["id"]
        dna = seq["sequence"].upper()

        if seq_id in ids:
            errors.append("Duplicate sequence ID")

        ids.add(seq_id)

        if len(dna) == 0:
            errors.append("Empty sequence")

        invalid = sorted(set(dna) - VALID_BASES)

        if invalid:
            errors.append(
                "Invalid nucleotide(s): "
                + ", ".join(invalid)
            )

        report.append({
            "id": seq_id,
            "valid": len(errors) == 0,
            "errors": errors
        })

    return report