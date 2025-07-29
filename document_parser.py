import fitz  # PyMuPDF
from typing import List, Dict
import json
import os

def extract_chunks_from_pdf(pdf_path: str) -> List[Dict]:
    doc = fitz.open(pdf_path)
    chunks = []

    for page_num, page in enumerate(doc, start=1):
        text = page.get_text()
        
        # Split into smaller chunks by newline instead of large paragraphs
        lines = [line.strip() for line in text.split("\n") if len(line.strip()) > 40]

        for line in lines:
            chunks.append({
                "content": line,
                "source": f"Page {page_num}"
            })

    return chunks


def save_chunks_to_json(chunks: List[Dict], output_path: str):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    pdf_path = r"C:\Users\pulak\OneDrive\Documents\New folder\New folder\For Task - Policy file.pdf"
    os.makedirs("data", exist_ok=True)

    chunks = extract_chunks_from_pdf(pdf_path)
    save_chunks_to_json(chunks, "data/policy.json")

    print(f"✅ Extracted {len(chunks)} smaller chunks from the PDF and saved to data/policy.json")