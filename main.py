import os
import json
import pdfplumber
from collections import Counter

INPUT_DIR = "input"
OUTPUT_DIR = "output"

def extract_outline(pdf_path):
    outline = []
    title = ""
    font_sizes = []

    # Step 1: Collect font sizes
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            words = page.extract_words(extra_attrs=['size'])
            for word in words:
                font_sizes.append(word['size'])

    # Find largest sizes
    sizes_sorted = sorted(list(set(font_sizes)), reverse=True)
    title_size = sizes_sorted[0] if len(sizes_sorted) > 0 else None
    h1_size = sizes_sorted[1] if len(sizes_sorted) > 1 else None
    h2_size = sizes_sorted[2] if len(sizes_sorted) > 2 else None
    h3_size = sizes_sorted[3] if len(sizes_sorted) > 3 else None

    # Step 2: Detect headings
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            words = page.extract_words(extra_attrs=['size'])

            for word in words:
                text = word['text'].strip()
                size = word['size']

                if size == title_size and not title and i == 0:
                    title = text

                elif size == h1_size:
                    outline.append({
                        "level": "H1",
                        "text": text,
                        "page": i + 1
                    })
                elif size == h2_size:
                    outline.append({
                        "level": "H2",
                        "text": text,
                        "page": i + 1
                    })
                elif size == h3_size:
                    outline.append({
                        "level": "H3",
                        "text": text,
                        "page": i + 1
                    })

    return {
        "title": title,
        "outline": outline
    }

def main():
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(INPUT_DIR, filename)
            result = extract_outline(pdf_path)

            output_filename = filename.replace(".pdf", ".json")
            output_path = os.path.join(OUTPUT_DIR, output_filename)

            with open(output_path, "w") as f:
                json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()
