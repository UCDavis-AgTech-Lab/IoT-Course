# TAE30 – Communications & Computing Technology  
_Internet of Things (IoT) Laboratory Materials_

[![Live Site](https://img.shields.io/badge/GitHub%20Pages-live-blue)](https://ucdavis-agtech-lab.github.io/IoT-Course/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](#license)

Interactive course website and lab content for **TAE30: Communications and Computing Technology** offered by the University of California, Davis (Biological & Agricultural Engineering).  
The goal is to provide a self‑contained, modern learning hub that guides students from IoT fundamentals to a complete Smart Pot project using Parallax Propeller Activity Board WX.

---

## ✨ Key Features
| Feature | Description |
|---------|-------------|
| 📑 **Modular Architecture** | Separated HTML, CSS, and JavaScript files for professional maintainability. |
| 🌓 **Light / Dark Theme** | One‑click theme toggle with preference stored in `localStorage`. |
| 🖨️ **Print / PDF‑ready** | "Download as PDF" button isolates the current section and triggers `window.print()` for clean exports. |
| 📝 **Markdown Export** | "Download as MD" converts the visible section to Markdown and downloads it as a file. |
| 📱 **Responsive Design** | Collapsible sidebar and mobile dropdown keep navigation usable on any screen size. |
| 🗺️ **Progressive Lab Series** | 10 complete labs + Smart Pot capstone project with BlocklyProp Solo programming. |
| 🛠️ **Hardware Documentation** | Comprehensive Parallax Propeller board documentation and custom board specs. |
| 🗃️ **Course Materials** | Syllabus, resources, FAQ, and all lab content organized professionally. |
| 🚀 **Dynamic Loading** | JavaScript dynamically loads page content without page refreshes. |
| 📊 **Smart Agriculture Focus** | Real-world IoT applications in agricultural and environmental monitoring. |

---

## 🚀 Live Demo
The production build is automatically published via GitHub Pages:  
<https://ucdavis-agtech-lab.github.io/IoT-Course/>

---

## 🖥️ Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/MohammadrezaNarimaniUCDavis/TAE30-IoT-Lab-Materials.git
cd TAE30-IoT-Lab-Materials

# 2. Serve locally (Python 3)
python -m http.server 8000
# then visit http://localhost:8000 in your browser
```

_No dependencies are required—any static file server (or just opening `index.html`) will work._

---

## 🔧 Project Structure
```
├── index.html              # main website file
├── css/
│   └── styles.css          # all styling
├── js/
│   └── main.js             # all functionality
├── pages/                  # individual page content
│   ├── syllabus.html
│   ├── resources.html
│   ├── faq.html
│   ├── hardware*.html      # hardware documentation
│   └── lab1-lab10.html     # lab materials
├── assets/                 # images and media
│   └── images/
│       ├── logos/
│       ├── people/
│       ├── hardware/       # board diagrams & schematics
│       └── learning-modules/ # lab screenshots & diagrams
└── README.md               # you're reading it!
```

---

## 📚 Course Overview

The course introduces IoT fundamentals using **Parallax Propeller Activity Board WX** and **BlocklyProp Solo** visual programming. Students progress through hands-on laboratories covering:

### 🔬 Laboratory Sessions
1. **Lab 1**: Installing BlocklyProp Solo - Development environment setup
2. **Lab 2**: Blockly Programming - Variables, functions, loops, conditionals  
3. **Lab 3**: Temperature Conversion & Password Evaluator - Advanced programming with functions and boolean logic
4. **Lab 4**: Temperature & Humidity Sensor - Environmental sensor integration with DHT22
5. **Lab 5**: Ping Sensor, Speaker & LED - Proximity detection with audio feedback and distance measurement
6. **Lab 6**: PAR & Soil Moisture Sensors - Agricultural sensor integration for light and moisture monitoring
7. **Lab 7**: Controlling Actuators - Servo motors and pumps based on sensor measurements
8. **Lab 8 Part 1**: Sensor Accuracy Evaluation - Compare Ultrasonic vs. Laser Ping sensors with Excel analysis
9. **Lab 8 Part 2**: Sensor Calibration - Learn calibration techniques and characteristic curve analysis
10. **Lab 9**: IoT Dashboard - Build real-time data logging and web-based IoT dashboards with ChatGPT
11. **Lab 10**: Smart Pot Project - Complete IoT system for plant environment control

### 🛠️ Hardware Documentation
- **Parallax Propeller Board Overview** - Key features and setup guide
- **Detailed Board Breakdown** - Complete technical specifications and pin assignments
- **Custom Green Board** - Course-specific development board documentation

### 🌱 Capstone Project: Smart Pot
Students build a complete IoT-controlled plant environment system featuring:
- **Multi-sensor Integration**: Temperature/RH, PAR light, soil moisture sensors
- **Automated Control**: Servo motors, irrigation pumps, LED lighting
- **Threshold-based Logic**: User-defined environmental parameters
- **Real-time Monitoring**: Terminal-based system status and sensor readings

---

## 🎯 Learning Outcomes

By completing this course, students will be able to:
- Program microcontrollers using visual block-based programming (BlocklyProp Solo)
- Integrate multiple sensors for environmental monitoring
- Implement automated control systems with actuators
- Design IoT solutions for agricultural applications
- Debug and troubleshoot embedded systems
- Apply threshold-based decision making in IoT systems

---

## 🤝 Contributing

1. **Fork** the repository  
2. **Create** your feature branch (`git checkout -b feature/my-feature`)  
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)  
4. **Push** to the branch (`git push origin feature/my-feature`)  
5. **Open a Pull Request**

Please use the **Open Issue** button in the site header or the GitHub "Issues" tab for bugs or enhancement ideas.

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

## 🙏 Acknowledgements

* **UC Davis Biological & Agricultural Engineering** – course host  
* **Parallax Inc.** – BlocklyProp Solo platform and Activity Board WX hardware
* **Previous Course Materials** – Foundation content from earlier course iterations
* GitHub Pages – free static site hosting  
