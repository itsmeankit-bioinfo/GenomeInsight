from genomeinsight.analysis.transcription import transcribe


def register(subparsers):
    parser = subparsers.add_parser(
        "transcribe",
        help="Transcribe DNA into RNA"
    )

    parser.add_argument(
        "sequence",
        help="DNA sequence"
    )

    parser.set_defaults(func=run)


def run(args):
    rna = transcribe(args.sequence)

    print(f"DNA Sequence : {args.sequence.upper()}")
    print(f"RNA Sequence : {rna}")