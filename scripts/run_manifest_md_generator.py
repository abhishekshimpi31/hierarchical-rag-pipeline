import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import config
from src.ingestion.manifest_mdfile_generation import extract_document_context

def main():
    PDF_FILE = "data/pdf_files/IPCC_AR6_WGI_Chapter04.pdf"
    output_dir = "data/extracted_data/"
    extract_document_context(pdf_path=PDF_FILE, base_output_dir=output_dir)

if __name__ == "__main__":
    main()
