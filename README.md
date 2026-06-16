# PDF Outline Extractor

## Overview

PDF Outline Extractor is a Python-based document analysis tool that automatically extracts document titles and hierarchical headings (H1, H2, H3) from PDF files and generates a structured JSON outline. The project combines rule-based PDF parsing with machine learning experimentation to identify document structure and improve information extraction from unstructured PDF documents.

The system is designed for document preprocessing, content indexing, knowledge management systems, and downstream Natural Language Processing (NLP) applications.

---

## Features

* Extract document title automatically
* Detect hierarchical headings (H1, H2, H3)
* Generate structured JSON output
* Parse PDF documents using font size analysis
* Machine Learning experimentation using DistilBERT
* Docker support for containerized execution
* Lightweight and easy to integrate into existing workflows

---

## Project Structure

```text
pdf_outline_extractor/
│
├── extractor.py
├── train.py
├── requirements.txt
├── Dockerfile
├── dataset/
├── models/
├── input/
├── output/
└── README.md
```

---

## Technologies Used

* Python
* pdfplumber
* JSON
* Hugging Face Transformers
* DistilBERT
* Docker

---

## How It Works

### Rule-Based Extraction

1. Read PDF document.
2. Extract text blocks and font metadata.
3. Identify unique font sizes.
4. Assign:

   * Largest font → Title
   * Second largest → H1
   * Third largest → H2
   * Fourth largest → H3
5. Generate structured JSON output.

### Machine Learning Approach

The project also includes an experimental DistilBERT-based classifier trained to categorize extracted text into:

* Title
* H1
* H2
* H3
* Body Text

This enables future improvements beyond simple font-size heuristics.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/pdf-outline-extractor.git
cd pdf-outline-extractor
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Place PDF files inside the input directory.

Run the extractor:

```bash
python extractor.py
```

Generated JSON files will be available in:

```text
output/
```

Example Output:

```json
{
  "title": "Attention Is All You Need",
  "outline": [
    {
      "level": "H1",
      "text": "Introduction",
      "page": 1
    },
    {
      "level": "H2",
      "text": "Transformer Architecture",
      "page": 3
    }
  ]
}
```

---

## Machine Learning Training

To train the DistilBERT heading classifier:

```bash
python train.py
```

The trained model will be stored in the models directory.

---

## Applications

* Document Structure Analysis
* Knowledge Management Systems
* PDF Search Engines
* Intelligent Document Processing
* NLP Preprocessing Pipelines
* Research Paper Analysis
* Automated Content Indexing

---

## Future Enhancements

* Layout-aware heading detection
* OCR support for scanned PDFs
* Deep Learning based heading classification
* Support for tables and figures
* Web-based user interface
* Batch PDF processing
* Semantic document summarization

---
