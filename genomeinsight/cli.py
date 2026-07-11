import argparse

from genomeinsight import __version__

from genomeinsight.commands import (
    gc,
    reverse,
)


def main():
    parser = argparse.ArgumentParser(
        prog="genomeinsight",
        description="GenomeInsight - A Python toolkit for genomics and metagenomics"
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"GenomeInsight v{__version__}"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        metavar="<command>"
    )

    # Register commands
    gc.register(subparsers)
    reverse.register(subparsers)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()