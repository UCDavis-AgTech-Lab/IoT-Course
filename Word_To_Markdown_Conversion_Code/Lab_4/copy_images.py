#!/usr/bin/env python3
"""
Copy Lab 4 images to assets folder
"""

import shutil
from pathlib import Path

def copy_images():
    # Paths
    script_dir = Path(__file__).parent
    source_dir = script_dir / "../../Lab_Markdowns/Lab_4/media"
    target_dir = script_dir / "../../assets/images/learning-modules/Lab_4"
    
    # Create target directory
    target_dir.mkdir(parents=True, exist_ok=True)
    
    # Copy all images
    for image_file in source_dir.glob("*"):
        if image_file.is_file():
            target_file = target_dir / image_file.name
            shutil.copy2(image_file, target_file)
            print(f"Copied: {image_file.name}")
    
    print(f"All images copied to: {target_dir}")

if __name__ == "__main__":
    copy_images()