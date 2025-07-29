import fitz  # PyMuPDF
from typing import List, Dict
import json

def extract_chunks_from_pdf(pdf_path: str) -> List[Dict]:
    doc = fitz.open(pdf_path)
    chunks = []

    for page_num, page in enumerate(doc, start=1):
        text = page.get_text()
        
        # Split text into paragraphs or large enough chunks
        paragraphs = [p.strip() for p in text.split("\n\n") if len(p.strip()) > 50]

        for para in paragraphs:
            chunks.append({
                "content": para,
                "source": f"Page {page_num}"
            })

    return chunks


def save_chunks_to_json(chunks: List[Dict], output_path: str):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    # Replace this with the exact path to your file using raw string format
    pdf_path = r"C:\Users\pulak\OneDrive\Documents\New folder\New folder\For Task - Policy file.pdf"
    
    # Optional: create the data directory if it doesn't exist
    import os
    os.makedirs("data", exist_ok=True)

    chunks = extract_chunks_from_pdf(pdf_path)
    save_chunks_to_json(chunks, "data/policy.json")

    print(f"✅ Extracted {len(chunks)} chunks from the PDF and saved to data/policy.json")
