"""
FASTQ quality analysis.
"""


def quality_statistics(reads):

    scores = []

    total_bases = 0
    q20 = 0
    q30 = 0

    for read in reads:

        for char in read["quality"]:

            score = ord(char) - 33

            scores.append(score)

            total_bases += 1

            if score >= 20:
                q20 += 1

            if score >= 30:
                q30 += 1

    if not scores:

        return {
            "average": 0,
            "minimum": 0,
            "maximum": 0,
            "q20": 0,
            "q30": 0,
            "q20_percent": 0,
            "q30_percent": 0,
        }

    return {
        "average": sum(scores) / len(scores),
        "minimum": min(scores),
        "maximum": max(scores),
        "q20": q20,
        "q30": q30,
        "q20_percent": q20 / total_bases * 100,
        "q30_percent": q30 / total_bases * 100,
    }