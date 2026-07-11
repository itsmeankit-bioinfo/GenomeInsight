"""
Smith-Waterman Local Alignment
"""

MATCH = 2
MISMATCH = -1
GAP = -2


def smith_waterman(seq1: str, seq2: str):

    seq1 = seq1.upper()
    seq2 = seq2.upper()

    rows = len(seq1) + 1
    cols = len(seq2) + 1

    score = [[0] * cols for _ in range(rows)]

    max_score = 0
    max_i = 0
    max_j = 0

    for i in range(1, rows):

        for j in range(1, cols):

            diagonal = score[i-1][j-1] + (
                MATCH if seq1[i-1] == seq2[j-1] else MISMATCH
            )

            up = score[i-1][j] + GAP
            left = score[i][j-1] + GAP

            score[i][j] = max(0, diagonal, up, left)

            if score[i][j] > max_score:
                max_score = score[i][j]
                max_i = i
                max_j = j

    aligned1 = []
    aligned2 = []

    i = max_i
    j = max_j

    while i > 0 and j > 0 and score[i][j] != 0:

        if score[i][j] == score[i-1][j-1] + (
            MATCH if seq1[i-1] == seq2[j-1] else MISMATCH
        ):

            aligned1.append(seq1[i-1])
            aligned2.append(seq2[j-1])

            i -= 1
            j -= 1

        elif score[i][j] == score[i-1][j] + GAP:

            aligned1.append(seq1[i-1])
            aligned2.append("-")
            i -= 1

        else:

            aligned1.append("-")
            aligned2.append(seq2[j-1])
            j -= 1

    aligned1.reverse()
    aligned2.reverse()

    return {
        "score": max_score,
        "seq1": "".join(aligned1),
        "seq2": "".join(aligned2),
    }