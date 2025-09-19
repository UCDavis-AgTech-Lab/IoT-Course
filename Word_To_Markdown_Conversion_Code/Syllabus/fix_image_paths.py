import re

def fix_image_paths():
    # Read the markdown file
    md_file = r"C:\mnarimani\1-UCDavis\9-Github\TAE30-IoT-Lab-Materials\Course_Instruction_Markdown\syllabus_content.md"
    
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix image paths - change from media/image1.png to ../assets/images/course-instruction/image1.png
    content = re.sub(r'!\[(.*?)\]\(media/(.*?)\)', r'![\1](../assets/images/course-instruction/\2)', content)
    
    # Write back the fixed content
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Fixed image paths in syllabus markdown")

if __name__ == "__main__":
    fix_image_paths()