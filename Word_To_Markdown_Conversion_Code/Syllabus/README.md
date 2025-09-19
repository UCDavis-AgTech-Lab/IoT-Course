# Syllabus Conversion Instructions

## Step 1: Convert Word to Markdown
```bash
cd "C:\mnarimani\1-UCDavis\9-Github\TAE30-IoT-Lab-Materials\Word_To_Markdown_Conversion_Code\Syllabus"
python convert_syllabus.py
```

## Step 2: Fix Image Paths
```bash
python fix_image_paths.py
```

## Step 3: Copy Images to Assets
```bash
python copy_images.py
```

## Files Created:
- `C:\mnarimani\1-UCDavis\9-Github\TAE30-IoT-Lab-Materials\Course_Instruction_Markdown\syllabus_content.md`
- Images in `C:\mnarimani\1-UCDavis\9-Github\TAE30-IoT-Lab-Materials\assets\images\course-instruction\`

## Next Steps:
After conversion, you can split the markdown content into separate sections for:
- Home page content
- Syllabus page content  
- Resources page content
- FAQ page content