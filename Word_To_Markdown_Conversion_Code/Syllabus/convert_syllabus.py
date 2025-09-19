import subprocess
import os

def convert_syllabus():
    # Input and output paths
    input_docx = r"C:\mnarimani\1-UCDavis\9-Github\TAE30-IoT-Lab-Materials\Course_Instruction_PDF\Syllabus_TAE_30_Spring_2024.docx"
    output_md = r"C:\mnarimani\1-UCDavis\9-Github\TAE30-IoT-Lab-Materials\Course_Instruction_Markdown\syllabus_content.md"
    media_dir = r"C:\mnarimani\1-UCDavis\9-Github\TAE30-IoT-Lab-Materials\Course_Instruction_Markdown"
    
    # Pandoc command to convert Word to Markdown with image extraction
    cmd = [
        "pandoc",
        input_docx,
        "-o", output_md,
        "--extract-media", media_dir,
        "--wrap=none"
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"✅ Successfully converted syllabus to: {output_md}")
        print(f"📁 Images extracted to: {media_dir}")
        
        if result.stdout:
            print("STDOUT:", result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during conversion: {e}")
        print(f"Return code: {e.returncode}")
        if e.stdout:
            print("STDOUT:", e.stdout)
        if e.stderr:
            print("STDERR:", e.stderr)
    except FileNotFoundError:
        print("❌ Pandoc not found. Please install Pandoc first.")

if __name__ == "__main__":
    convert_syllabus()