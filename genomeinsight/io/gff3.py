"""
Simple GFF3 parser.
"""


def read_gff3(file_path):

    features = []

    with open(file_path) as file:

        for line in file:

            line = line.strip()

            if not line:
                continue

            if line.startswith("#"):
                continue

            fields = line.split("\t")

            if len(fields) != 9:
                continue

            features.append({
                "seqid": fields[0],
                "source": fields[1],
                "type": fields[2],
                "start": int(fields[3]),
                "end": int(fields[4]),
                "score": fields[5],
                "strand": fields[6],
                "phase": fields[7],
                "attributes": fields[8],
            })

    return features