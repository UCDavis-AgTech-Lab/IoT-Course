@echo off
echo Creating dev branch and pushing all files...

REM Create and switch to dev branch
git checkout -b dev

REM Add all files to staging
git add .

REM Commit all changes
git commit -m "Create dev branch with updated website content - banner images, syllabus updates, header styling, and IoT Farm branding"

REM Push dev branch to GitHub
git push -u origin dev

echo.
echo Dev branch created and pushed successfully!
echo You can now switch between branches using:
echo   git checkout main    (for main branch)
echo   git checkout dev     (for dev branch)

pause