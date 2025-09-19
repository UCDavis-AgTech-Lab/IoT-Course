# TAE30 IoT Lab Materials - AI Assistant Context

## Project Overview
This is a comprehensive educational website for **TAE30: Communications & Computing Technology** course at UC Davis. The project provides interactive IoT laboratory materials using Parallax Propeller Activity Board WX and BlocklyProp Solo programming.

## What We Built
- **Complete Course Website**: Modern, responsive web interface with 10+ lab modules
- **Progressive Learning Path**: From basic programming to complete IoT systems
- **Smart Agriculture Focus**: Real-world applications in agricultural monitoring and control
- **Multi-Modal Content**: HTML pages, images, interactive elements, and downloadable resources

## Technical Architecture

### Frontend Structure
```
├── index.html              # Main website with dynamic navigation
├── css/styles.css          # Complete styling with UC Davis branding
├── js/main.js              # Dynamic page loading, theme toggle, PDF/MD export
├── pages/                  # Individual lab content (lab1.html - lab10.html)
├── assets/images/          # All visual content organized by lab
└── Lab_Markdowns/          # Source markdown files for each lab
```

### Content Conversion System
```
Word_To_Markdown_Conversion_Code/
├── Lab_1/ ... Lab_10/      # Automated conversion scripts
│   ├── convert_labX.py     # Pandoc Word→Markdown conversion
│   ├── fix_image_paths.py  # Fix relative image paths
│   └── copy_images.py      # Copy images to assets folder
```

## Laboratory Progression

### Foundation Labs (1-3)
- **Lab 1**: BlocklyProp Solo installation and setup
- **Lab 2**: Basic Blockly programming (variables, functions, loops)
- **Lab 3**: Advanced programming (temperature conversion, password systems)

### Sensor Integration Labs (4-6)
- **Lab 4**: DHT22 temperature/humidity sensor with LED control
- **Lab 5**: Laser ping sensor with audio feedback and distance measurement
- **Lab 6**: PAR and soil moisture sensors for agricultural monitoring

### Advanced IoT Labs (7-10)
- **Lab 7**: Actuator control (servo motors, peristaltic pumps, relay modules)
- **Lab 8 Part 1**: Sensor accuracy evaluation with Excel data analysis
- **Lab 8 Part 2**: Sensor calibration techniques and characteristic curves
- **Lab 9**: IoT dashboard creation using ChatGPT and Wi-Fi modules
- **Lab 10**: Smart Pot capstone project (complete IoT system)

## Key Technologies Used
- **Hardware**: Parallax Propeller Activity Board WX, ESP8266 Wi-Fi module
- **Programming**: BlocklyProp Solo (visual programming), Simple IDE (C)
- **Sensors**: DHT22, PAR, soil moisture, ultrasonic, laser ping
- **Actuators**: Servo motors, peristaltic pumps, LEDs, relay modules
- **Web Tech**: HTML5, CSS3, JavaScript ES6, Chart.js, responsive design
- **Tools**: Pandoc (document conversion), Excel (data analysis), ChatGPT (dashboard generation)

## Smart Pot Capstone Project
The final project integrates all course concepts into a complete IoT system:
- **Multi-sensor monitoring**: Temperature, humidity, light (PAR), soil moisture
- **Automated control**: Fan (LED), window (servo), irrigation (pump), lighting (relay)
- **Threshold-based logic**: User-defined environmental parameters
- **Real-time feedback**: Terminal display with iteration counting

## Content Management Workflow

### Adding New Labs
1. Place Word document in `Lab_PDFs/X-Week_X/`
2. Run conversion scripts: `convert_labX.py → fix_image_paths.py → copy_images.py`
3. Create `pages/labX.html` using consistent styling structure
4. Update navigation in `index.html` and `js/main.js`

### Styling Consistency
All labs follow identical structure:
- `lab-section-title` for main headings
- `card` containers for content blocks
- `step` and `step-title` for tutorials
- `lab-image` class for all images
- `highlight` class for important text

## AI Assistant Instructions

### When Working on This Project:
1. **Maintain Consistency**: All new content must match existing styling patterns
2. **Follow Structure**: Use established HTML/CSS classes and layout patterns
3. **Update Navigation**: Always update both `index.html` sidebar and `js/main.js` mappings
4. **Image Management**: Place images in `assets/images/learning-modules/Lab_X/`
5. **Responsive Design**: Ensure all content works on mobile and desktop

### Common Tasks:
- **Adding Labs**: Follow the conversion workflow above
- **Updating Content**: Modify both markdown source and HTML pages
- **Fixing Styling**: Check against other labs for consistency
- **Adding Features**: Update `main.js` for new functionality

### Project Goals:
- **Educational Excellence**: Clear, progressive learning path
- **Professional Quality**: Modern web standards and UC Davis branding
- **Practical Application**: Real-world IoT skills for agriculture
- **Accessibility**: Works across devices and browsers

## Future Development Opportunities
- **Interactive Simulations**: BlocklyProp code simulators
- **Video Integration**: Embedded lab demonstration videos
- **Progress Tracking**: Student completion tracking system
- **Mobile App**: Companion mobile application
- **Advanced Projects**: Additional capstone project options
- **Multilingual Support**: Spanish/other language versions

This project represents a complete educational IoT curriculum with modern web delivery, suitable for university-level engineering education.