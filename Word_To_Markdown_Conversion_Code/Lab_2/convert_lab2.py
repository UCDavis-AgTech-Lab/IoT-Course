#!/usr/bin/env python3
"""
Convert Lab 2 Word document to Markdown using pandoc
"""

import subprocess
import os
import sys
from pathlib import Path

def main():
    print("Converting Lab 2 Word document to Markdown...")
    
    # Set paths
    script_dir = Path(__file__).parent
    input_file = script_dir / "../../Lab_PDFs/2-Week_2/Lab_2_programming_odd_even.docx"
    output_dir = script_dir / "../../Lab_Markdowns/Lab_2"
    output_file = output_dir / "Lab_2_programming_odd_even.md"
    
    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Check if pandoc is installed
    pandoc_path = r"C:\Program Files\Pandoc\pandoc.exe"
    try:
        result = subprocess.run([pandoc_path, "--version"], capture_output=True, text=True)
        print(f"Pandoc found: {result.stdout.split()[1]}")
    except FileNotFoundError:
        print("ERROR: Pandoc not found at expected location.")
        print(f"Expected: {pandoc_path}")
        sys.exit(1)
    
    # Check if input file exists
    if not input_file.exists():
        print(f"ERROR: Input file not found: {input_file}")
        sys.exit(1)
    
    # Run pandoc conversion
    cmd = [
        pandoc_path,
        str(input_file),
        "--from=docx",
        "--to=markdown",
        f"--output={output_file}",
        f"--extract-media={output_dir}",
        "--wrap=none",
        "--markdown-headings=atx"
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print("Conversion complete!")
        print(f"Output file: {output_file}")
        print(f"Images extracted to: {output_dir}/media")
        
        # Show file info
        if output_file.exists():
            size = output_file.stat().st_size
            print(f"Markdown file size: {size} bytes")
        
        # List extracted images
        media_dir = output_dir / "media"
        if media_dir.exists():
            images = list(media_dir.rglob("*"))
            if images:
                print(f"Extracted {len(images)} files:")
                for img in images:
                    print(f"  - {img.name}")
        
    except subprocess.CalledProcessError as e:
        print(f"ERROR during conversion: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()