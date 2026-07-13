# 🧬 GenomeInsight

A modern command-line toolkit for bioinformatics sequence analysis, genome annotation, and molecular biology workflows.

GenomeInsight provides fast, lightweight, and easy-to-use tools for working with DNA, RNA, and protein sequences directly from the command line.

---

## ✨ Features

### 🧬 Sequence Analysis

- GC Content
- Reverse Complement
- DNA → RNA Transcription
- DNA → Protein Translation
- Open Reading Frame (ORF) Finder
- K-mer Analysis
- Motif Search

---

### 🧪 Primer Design

- Primer Statistics
- Melting Temperature (Tm)
- GC Percentage
- Primer Length

---

### 🔬 Restriction Enzyme Analysis

- Restriction Site Detection
- Enzyme Recognition Analysis

---

### 📁 File Format Support

- FASTA
- FASTQ
- GFF

---

### 🧬 Protein Analysis

- Protein Summary
- Amino Acid Composition
- Molecular Weight
- Isoelectric Point (pI)
- GRAVY (Hydrophobicity)
- Aromaticity
- Instability Index

---

### 🧪 Sequence Alignment

- Global Alignment
- Local Alignment

---

### 📊 Quality Control

- Read Quality Statistics
- N50 Calculation
- FastQC Integration

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/itsmeankit-bioinfo/GenomeInsight.git
cd GenomeInsight
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -e .
```

---

## 🚀 Usage

Display help

```bash
genomeinsight --help
```

---

## 🧬 DNA Commands

GC Content

```bash
genomeinsight gc examples/sample.fasta
```

Reverse Complement

```bash
genomeinsight reverse examples/sample.fasta
```

Transcription

```bash
genomeinsight transcribe examples/sample.fasta
```

Translation

```bash
genomeinsight translate examples/sample.fasta
```

ORF Finder

```bash
genomeinsight orf examples/sample.fasta
```

Motif Search

```bash
genomeinsight motif examples/sample.fasta ATG
```

K-mer Analysis

```bash
genomeinsight kmer examples/sample.fasta 4
```

---

## 🧪 Primer Analysis

```bash
genomeinsight primer ACTGACTGACTG
```

---

## 🔬 Restriction Analysis

```bash
genomeinsight restriction examples/sample.fasta
```

---

## 📁 File Utilities

FASTA Information

```bash
genomeinsight fasta examples/sample.fasta
```

FASTQ Statistics

```bash
genomeinsight fastq examples/sample.fastq
```

GFF Summary

```bash
genomeinsight gff examples/sample.gff
```

---

## 🧬 Protein Analysis

Protein Summary

```bash
genomeinsight protein info examples/protein.fasta
```

Amino Acid Composition

```bash
genomeinsight protein composition examples/protein.fasta
```

Molecular Weight

```bash
genomeinsight protein mw examples/protein.fasta
```

Isoelectric Point

```bash
genomeinsight protein pi examples/protein.fasta
```

GRAVY

```bash
genomeinsight protein gravy examples/protein.fasta
```

Aromaticity

```bash
genomeinsight protein aromaticity examples/protein.fasta
```

Instability Index

```bash
genomeinsight protein instability examples/protein.fasta
```

---

## 📊 Quality Control

N50

```bash
genomeinsight n50 assembly.fasta
```

Read Quality

```bash
genomeinsight quality reads.fastq
```

FastQC

```bash
genomeinsight fastqc reads.fastq
```

---

## 🧪 Sequence Alignment

Global Alignment

```bash
genomeinsight align seq1.fasta seq2.fasta
```

Local Alignment

```bash
genomeinsight localalign seq1.fasta seq2.fasta
```

---

## 🛠️ Technology Stack

- Python 3.11+
- BioPython
- Click
- Pytest
- Ruff
- GitHub Actions

---

## 🧪 Testing

Run all tests

```bash
python -m pytest -v
```

Run Ruff

```bash
python -m ruff check .
```

---

## 📂 Project Structure

```
GenomeInsight/
│
├── genomeinsight/
│   ├── analysis/
│   ├── commands/
│   ├── io/
│   └── utils/
│
├── tests/
├── examples/
├── docs/
├── .github/
└── README.md
```

---

## 📈 Current Status

Current Version

**v0.2.0**

Implemented

- ✅ 35 Automated Tests
- ✅ GitHub Actions CI
- ✅ Ruff Linting
- ✅ Modular CLI Architecture
- ✅ DNA Analysis
- ✅ Protein Analysis
- ✅ File Parsers
- ✅ Sequence Alignment
- ✅ Quality Control Tools

---

## 🚀 Roadmap

Upcoming features

- GenBank Parser
- VCF Parser
- SAM/BAM Statistics
- BLAST Output Parser
- Phylogenetic Analysis
- HTML Reports
- Workflow Pipeline
- Plugin System

---

## 🤝 Contributing

Contributions, feature requests, and bug reports are welcome.

---

## 📄 License

MIT License

---

## 👨‍💻 Author

**Ankit Raj**

M.Sc. Bioinformatics

GenomeInsight is an open-source bioinformatics toolkit developed for learning, research, and genomics workflows.