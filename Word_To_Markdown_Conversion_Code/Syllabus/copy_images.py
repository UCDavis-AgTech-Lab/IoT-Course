import shutil
import os
import glob

def copy_images():
    # Source and destination directories
    source_dir = r"C:\mnarimani\1-UCDavis\9-Github\TAE30-IoT-Lab-Materials\Course_Instruction_Markdown\media"
    dest_dir = r"C:\mnarimani\1-UCDavis\9-Github\TAE30-IoT-Lab-Materials\assets\images\course-instruction"
    
    # Create destination directory if it doesn't exist
    os.makedirs(dest_dir, exist_ok=True)
    
    # Copy all images from source to destination
    if os.path.exists(source_dir):
        image_files = glob.glob(os.path.join(source_dir, "*"))
        
        for image_file in image_files:
            if os.path.isfile(image_file):
                filename = os.path.basename(image_file)
                dest_path = os.path.join(dest_dir, filename)
                shutil.copy2(image_file, dest_path)
                print(f"📁 Copied: {filename}")
        
        print(f"✅ All images copied to: {dest_dir}")
    else:
        print(f"❌ Source directory not found: {source_dir}")

if __name__ == "__main__":
    copy_images()