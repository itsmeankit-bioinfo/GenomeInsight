"""
ORF Finder for GenomeInsight.
"""


STOP_CODONS = {"TAA", "TAG", "TGA"}
START_CODON = "ATG"


def find_orfs(sequence: str):
    """
    Find all ORFs in the first reading frame.
    """

    sequence = sequence.upper()

    orfs = []

    i = 0

    while i <= len(sequence) - 3:

        codon = sequence[i:i + 3]

        if codon == START_CODON:

            j = i + 3

            while j <= len(sequence) - 3:

                stop = sequence[j:j + 3]

                if stop in STOP_CODONS:

                    orfs.append({
                        "start": i + 1,
                        "end": j + 3,
                        "sequence": sequence[i:j + 3]
                    })

                    break

                j += 3

        i += 1

    return orfs