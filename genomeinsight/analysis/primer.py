from genomeinsight.analysis.gc_content import calculate_gc


def primer_analysis(sequence: str):

    sequence = sequence.upper()

    length = len(sequence)

    gc = calculate_gc(sequence)

    at = 100 - gc

    a = sequence.count("A")
    t = sequence.count("T")
    g = sequence.count("G")
    c = sequence.count("C")

    tm = 2 * (a + t) + 4 * (g + c)

    gc_clamp = sequence.endswith(("G", "C"))

    return {
        "length": length,
        "gc": gc,
        "at": at,
        "tm": tm,
        "gc_clamp": gc_clamp,
    }