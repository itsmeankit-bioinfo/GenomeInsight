"""
Export utilities for GenomeInsight.
"""

import csv


def export_csv(variants, output_file):
    """
    Export variants to a CSV file.

    Parameters
    ----------
    variants : list
        Parsed variants.

    output_file : str
        Output CSV filename.
    """

    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(
            [
                "Chromosome",
                "Position",
                "Reference",
                "Alternate",
            ]
        )

        for variant in variants:
            writer.writerow(
                [
                    variant["chrom"],
                    variant["pos"],
                    variant["ref"],
                    variant["alt"],
                ]
            )