"""
FastQC wrapper.
"""

import subprocess
from pathlib import Path


def run_fastqc(input_file, output_dir="fastqc_report"):

    Path(output_dir).mkdir(exist_ok=True)

    command = [
        "fastqc",
        input_file,
        "-o",
        output_dir,
    ]

    subprocess.run(command, check=True)

    return output_dir