# 🧬 GenomeInsight

![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-orange.svg)
![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen.svg)

A modern Python command-line toolkit for **genomics, sequence analysis, and bioinformatics workflows**.

GenomeInsight provides an easy-to-use CLI for performing common bioinformatics analyses including sequence statistics, FASTA/FASTQ parsing, ORF detection, motif searching, primer analysis, sequence alignment, and quality control.

---

# 🚀 Features

## Sequence Analysis

- ✅ GC Content Calculation
- ✅ Reverse Complement
- ✅ DNA → RNA Transcription
- ✅ DNA → Protein Translation
- ✅ Sequence Statistics

---

## File Processing

- ✅ FASTA Parser
- ✅ FASTQ Parser
- ✅ FASTA Validation
- ✅ GFF Parser

---

## Bioinformatics Algorithms

- ✅ ORF Finder
- ✅ K-mer Counter
- ✅ Motif Search
- ✅ Restriction Enzyme Analysis
- ✅ Primer Analysis
- ✅ Global Sequence Alignment
- ✅ Local Sequence Alignment
- ✅ N50 Calculation
- ✅ Read Quality Analysis

---

## External Tool Integration

- ✅ FastQC

Upcoming integrations:

- ⏳ Fastp
- ⏳ BWA
- ⏳ SAMtools
- ⏳ SPAdes
- ⏳ QUAST
- ⏳ Prokka
- ⏳ BLAST

---

## Protein Analysis (In Progress)

- ✅ Molecular Weight
- ✅ Isoelectric Point (pI)
- ✅ Aromaticity
- ✅ Instability Index
- ✅ GRAVY Score
- ⏳ Amino Acid Composition
- ⏳ Extinction Coefficient

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/itsmeankit-bioinfo/GenomeInsight.git

cd GenomeInsight
```

Install dependencies

```bash
python -m pip install -r requirements.txt
```

Install GenomeInsight

```bash
python -m pip install -e .
```

Verify installation

```bash
genomeinsight --version
```

---

# ⚡ Quick Start

Calculate GC content

```bash
genomeinsight gc ACTGACTG
```

Reverse complement

```bash
genomeinsight reverse ACTGACTG
```

DNA transcription

```bash
genomeinsight transcribe ACTGACTG
```

DNA translation

```bash
genomeinsight translate ATGGCC
```

Sequence statistics

```bash
genomeinsight stats ACTGACTG
```

Read a FASTA file

```bash
genomeinsight fasta examples/sample.fasta
```

Read a FASTQ file

```bash
genomeinsight fastq examples/sample.fastq
```

Find ORFs

```bash
genomeinsight orf examples/sample.fasta
```

Find Motifs

```bash
genomeinsight motif examples/sample.fasta ATG
```

Count K-mers

```bash
genomeinsight kmer examples/sample.fasta 4
```

Run FastQC

```bash
genomeinsight fastqc examples/sample.fastq
```

Protein Analysis

```bash
genomeinsight protein examples/protein.fasta
```

---

# 📂 Project Structure

```
GenomeInsight/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── docs/
├── examples/
├── tests/
│
├── genomeinsight/
│   ├── analysis/
│   ├── commands/
│   ├── io/
│   ├── pipeline/
│   ├── utils/
│   ├── cli.py
│   └── __init__.py
│
├── README.md
├── LICENSE
├── requirements.txt
├── pyproject.toml
└── pytest.ini
```

---

# 🧪 Testing

Run all tests

```bash
python -m pytest -v
```

Run Ruff

```bash
python -m ruff check .
```

---

# ⚙️ Continuous Integration

GenomeInsight uses **GitHub Actions** for automated testing.

Every push automatically:

- Installs dependencies
- Runs Ruff
- Executes all unit tests

---

# 🛠 Technologies Used

- Python
- BioPython
- Pytest
- Ruff
- GitHub Actions
- argparse

---

# 📈 Development Roadmap

## Version 0.2

- Protein Analysis Module
- GenBank Parser
- VCF Parser
- Multiple Sequence Alignment

---

## Version 0.3

- Phylogenetic Tree Construction
- HTML Reports
- Interactive Visualizations
- KEGG Integration

---

## Version 1.0

- Stable Release
- PyPI Package
- Conda Package
- Docker Support
- Plugin System

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/new-feature
```

3. Commit changes

```bash
git commit -m "Add new feature"
```

4. Push

```bash
git push origin feature/new-feature
```

5. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Ankit Raj**

M.Sc. Bioinformatics

GitHub:
https://github.com/itsmeankit-bioinfo

---

# ⭐ Support

If you find GenomeInsight useful, consider giving the repository a ⭐ on GitHub.

It helps others discover the project and supports future development.