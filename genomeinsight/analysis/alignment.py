"""
Needleman-Wunsch Global Alignment
"""


MATCH = 1
MISMATCH = -1
GAP = -1


def needleman_wunsch(seq1: str, seq2: str):

    seq1 = seq1.upper()
    seq2 = seq2.upper()

    rows = len(seq1) + 1
    cols = len(seq2) + 1

    score = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        score[i][0] = i * GAP

    for j in range(cols):
        score[0][j] = j * GAP

    for i in range(1, rows):

        for j in range(1, cols):

            diagonal = score[i - 1][j - 1]

            if seq1[i - 1] == seq2[j - 1]:
                diagonal += MATCH
            else:
                diagonal += MISMATCH

            up = score[i - 1][j] + GAP
            left = score[i][j - 1] + GAP

            score[i][j] = max(diagonal, up, left)

    aligned1 = []
    aligned2 = []

    i = len(seq1)
    j = len(seq2)

    while i > 0 or j > 0:

        if (
            i > 0
            and j > 0
        ):

            diagonal = score[i - 1][j - 1]

            if seq1[i - 1] == seq2[j - 1]:
                expected = diagonal + MATCH
            else:
                expected = diagonal + MISMATCH

            if score[i][j] == expected:

                aligned1.append(seq1[i - 1])
                aligned2.append(seq2[j - 1])

                i -= 1
                j -= 1

                continue

        if i > 0 and score[i][j] == score[i - 1][j] + GAP:

            aligned1.append(seq1[i - 1])
            aligned2.append("-")

            i -= 1

        else:

            aligned1.append("-")
            aligned2.append(seq2[j - 1])

            j -= 1

    aligned1.reverse()
    aligned2.reverse()

    return {
        "score": score[-1][-1],
        "seq1": "".join(aligned1),
        "seq2": "".join(aligned2),
    }