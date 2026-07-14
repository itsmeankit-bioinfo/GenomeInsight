# 🤝 Contributing to GenomeInsight

Thank you for your interest in contributing to **GenomeInsight**!

Whether you're fixing a bug, improving documentation, or adding a new bioinformatics feature, your contributions are welcome.

---

# 🚀 Getting Started

## 1. Fork the Repository

Fork the project on GitHub.

Then clone your fork:

```bash
git clone https://github.com/YOUR_USERNAME/GenomeInsight.git

cd GenomeInsight
```

---

## 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it.

### Windows

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -e .
```

---

# 🧪 Running Tests

Run all tests:

```bash
python -m pytest -v
```

Run Ruff:

```bash
python -m ruff check .
```

Before submitting a Pull Request, ensure:

- All tests pass
- Ruff reports no issues
- New functionality includes tests where appropriate

---

# 📂 Project Structure

```
genomeinsight/
├── analysis/
├── commands/
├── io/
├── pipeline/
└── utils/
```

- **analysis/** → Bioinformatics algorithms and calculations
- **commands/** → CLI command implementations
- **io/** → File parsers and readers
- **pipeline/** → Workflow automation
- **utils/** → Shared helper functions

---

# 💻 Coding Guidelines

Please follow these practices:

- Use meaningful variable names.
- Write clear docstrings for public functions.
- Keep functions focused on a single responsibility.
- Follow PEP 8 style guidelines.
- Keep imports at the top of the file.
- Run Ruff before committing.

---

# 🌱 Branch Naming

Examples:

```
feature/genbank-parser
feature/vcf-analysis
feature/html-report

bugfix/fasta-parser
bugfix/cli-error

docs/readme-update
docs/changelog
```

---

# 📝 Commit Messages

Use clear commit messages.

Examples:

```
feat: add VCF statistics command

fix: correct FASTA parsing bug

docs: update README

test: add GenBank parser tests

refactor: simplify protein analysis
```

---

# 🔀 Pull Requests

Before opening a Pull Request:

- Sync with the latest main branch.
- Run all tests.
- Run Ruff.
- Update documentation if necessary.
- Describe your changes clearly.

---

# 🐞 Reporting Issues

When reporting an issue, include:

- Operating system
- Python version
- GenomeInsight version
- Command executed
- Error message
- Steps to reproduce

---

# 💡 Suggesting Features

Feature requests are welcome.

Please describe:

- The problem
- Your proposed solution
- Expected behavior
- Example usage

---

# ❤️ Thank You

Thank you for helping improve GenomeInsight!

Every contribution, no matter how small, helps make the project better for the bioinformatics community.