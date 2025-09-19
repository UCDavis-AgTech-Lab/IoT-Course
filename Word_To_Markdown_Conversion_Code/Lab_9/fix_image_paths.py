#!/usr/bin/env python3
"""
Fix image paths in converted markdown file
"""

import re
from pathlib import Path

def fix_image_paths():
    # Paths
    script_dir = Path(__file__).parent
    md_file = script_dir / "../../Lab_Markdowns/Lab_9/Lab_7_IoT_Dashboard.md"
    
    print(f"Fixing image paths in: {md_file}")
    
    # Read the markdown file
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix image paths - replace absolute paths with relative paths
    pattern = r'!\[(.*?)\]\(C:\\.*?\\Lab_Markdowns\\Lab_9/media/(image\d+\.\w+)\)\{(.*?)\}'
    replacement = r'![\1](media/\2)'
    
    # Apply the replacement
    fixed_content = re.sub(pattern, replacement, content)
    
    # Also fix any remaining absolute paths without attributes
    pattern2 = r'!\[(.*?)\]\(C:\\.*?\\Lab_Markdowns\\Lab_9/media/(image\d+\.\w+)\)'
    replacement2 = r'![\1](media/\2)'
    fixed_content = re.sub(pattern2, replacement2, fixed_content)
    
    # Write back the fixed content
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print("Image paths fixed!")
    print("Images now use relative paths: media/imageX.ext")

if __name__ == "__main__":
    fix_image_paths()