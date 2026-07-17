# 🧬 GenomeInsight

![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-orange.svg)
![Status](https://img.shields.io/badge/Status-v0.3.0%20Released-success.svg)
![Tests](https://img.shields.io/badge/Tests-46%20Passing-success)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-blue)

A modern Python command-line toolkit for **genomics, sequence analysis, and bioinformatics workflows**.

GenomeInsight provides a modular command-line interface (CLI) for DNA, RNA, protein, genomics, and variant analysis. It includes sequence statistics, FASTA/FASTQ/GFF/GenBank/VCF parsing, ORF detection, motif searching, primer analysis, protein physicochemical analysis, sequence alignment, quality control, and workflow automation.

The project is designed as an open-source bioinformatics toolkit for students, researchers, and developers.

---

# 🚀 Features

## 🧬 Sequence Analysis

- ✅ GC Content Calculation
- ✅ Reverse Complement
- ✅ DNA → RNA Transcription
- ✅ DNA → Protein Translation
- ✅ Sequence Statistics

---

## 📁 File Processing

- ✅ FASTA Parser
- ✅ FASTQ Parser
- ✅ FASTA Validation
- ✅ GFF Parser
- ✅ GenBank Parser
- ✅ VCF Parser

---

## 🧪 Protein Analysis

- ✅ Protein Summary
- ✅ Amino Acid Composition
- ✅ Molecular Weight
- ✅ Isoelectric Point (pI)
- ✅ Aromaticity
- ✅ Instability Index
- ✅ GRAVY Score

---

## 🧬 Variant Analysis

- ✅ Variant Statistics
- ✅ SNP Extraction
- ✅ INDEL Extraction
- ✅ Chromosome Statistics
- ✅ VCF Summary
- ✅ Transition / Transversion Ratio
- ✅ Variant Filtering
- ✅ CSV Export
- ✅ JSON Export

---

## 🧬 Bioinformatics Algorithms

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

## ⚙️ External Tool Integration

- ✅ FastQC

Upcoming integrations

- ⏳ Fastp
- ⏳ BWA
- ⏳ SAMtools
- ⏳ SPAdes
- ⏳ QUAST
- ⏳ Prokka
- ⏳ BLAST

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

Protein Summary

```bash
genomeinsight protein info examples/protein.fasta
```

Protein Composition

```bash
genomeinsight protein composition examples/protein.fasta
```

Protein Molecular Weight

```bash
genomeinsight protein mw examples/protein.fasta
```

Protein Isoelectric Point

```bash
genomeinsight protein pi examples/protein.fasta
```
Protein GRAVY

```bash
genomeinsight protein gravy examples/protein.fasta
```

Protein Aromaticity

```bash
genomeinsight protein aromaticity examples/protein.fasta
```

Protein Instability

```bash
genomeinsight protein instability examples/protein.fasta
```

GenBank Summary

```bash
genomeinsight genbank info examples/sample.gb
```

GenBank Genes

```bash
genomeinsight genbank genes examples/sample.gb
```

GenBank Proteins

```bash
genomeinsight genbank proteins examples/sample.gb
```

VCF Summary

```bash
genomeinsight vcf summary examples/sample.vcf
```

SNP Extraction

```bash
genomeinsight vcf snps examples/sample.vcf
```

INDEL Extraction

```bash
genomeinsight vcf indels examples/sample.vcf
```

Chromosome Statistics

```bash
genomeinsight vcf chromosomes examples/sample.vcf
```

Transition / Transversion Ratio

```bash
genomeinsight vcf tstv examples/sample.vcf
```

Variant Filtering

```bash
genomeinsight vcf filter examples/sample.vcf --type snp
```

Export CSV

```bash
genomeinsight vcf export examples/sample.vcf --format csv
```

Export JSON

```bash
genomeinsight vcf export examples/sample.vcf --format json
```
---

# 📂 Project Structure

```text
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

# 📊 Current Project Status

Current Version

**v0.3.0**

### Statistics

- ✅ 46 Automated Tests
- ✅ Ruff Linting
- ✅ GitHub Actions CI
- ✅ Modular CLI Architecture

### Implemented Modules

- ✅ Sequence Analysis
- ✅ File Processing
- ✅ Protein Analysis
- ✅ GenBank Parser
- ✅ VCF Parser
- ✅ Variant Analysis
- ✅ Sequence Alignment
- ✅ Quality Control

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
- argparse
- Pytest
- Ruff
- Git
- GitHub
- GitHub Actions
- CSV
- JSON

---

# 📈 Development Roadmap

## Version 0.4

- ⏳ Multiple Sequence Alignment
- ⏳ Consensus Sequence
- ⏳ Alignment Statistics
- ⏳ BLAST Output Parser

---

## Version 0.5

- ⏳ Phylogenetic Analysis
- ⏳ Pipeline Engine
- ⏳ Workflow Automation
- ⏳ HTML Report Generation

---

## Version 1.0

- ⏳ Stable Release
- ⏳ PyPI Package
- ⏳ Conda Package
- ⏳ Docker Support
- ⏳ Plugin Architecture
- ⏳ Complete Documentation

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

---

## 📬 Contact

If you have suggestions, found a bug, or would like to contribute, feel free to:

- Open an Issue
- Submit a Pull Request
- Reach out through GitHub

Your feedback and contributions are always welcome.

---

## 🎯 Project Vision

GenomeInsight aims to become a comprehensive, open-source bioinformatics toolkit that simplifies sequence analysis, genomic data processing, and computational biology workflows through an easy-to-use command-line interface.

The project is designed for students, researchers, educators, and developers who want a lightweight yet powerful toolkit for everyday bioinformatics tasks.

---

🚀 **Building one module at a time toward a production-ready bioinformatics toolkit.**