# TAE 30 – Communications & Computing Technology  
_Internet of Things (IoT) Laboratory Materials_

[![Live Site](https://img.shields.io/badge/GitHub Pages-live-blue)](https://mohammadrezanarimaniucdavis.github.io/TAE30-IoT-Lab-Materials/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](#license)

Interactive course website and lab content for **TAE 30: Communications and Computing Technology** offered by the University of California, Davis (Biological & Agricultural Engineering).  
The goal is to provide a self‑contained, modern learning hub that guides students from IoT fundamentals to a full end‑to‑end project.

---

## ✨ Key Features
| Feature | Description |
|---------|-------------|
| 📑 **Single‑Page Web App** | Pure HTML/CSS/JS—no build tools—served via GitHub Pages for zero‑config deployment. |
| 🌓 **Light / Dark Theme** | One‑click theme toggle with preference stored in `localStorage`. |
| 🖨️ **Print / PDF‑ready** | “Download as PDF” button isolates the current section and triggers `window.print()` for clean exports. |
| 📝 **Markdown Export** | “Download as MD” converts the visible section (including tables, lists, images) to Markdown and downloads it as a file. |
| 📱 **Responsive Sidebar** | Collapsible sidebar and mobile dropdown keep navigation usable on any screen size. |
| 🗺️ **10 Modular Labs** | Each lab is its own anchor section with materials, images, and step‑by‑step instructions. |
| 🗃️ **Course Syllabus & Resources** | Built‑in syllabus table, reading list, online tutorials, and software download links. |
| 🛠️ **Vanilla JS Utilities** | JS handles routing (`history.pushState`), theme persistence, export helpers, and full‑screen mode—no frameworks needed. |

---

## 🚀 Live Demo
The production build is automatically published via GitHub Pages:  
<https://mohammadrezanarimaniucdavis.github.io/TAE30-IoT-Lab-Materials/>

---

## 🖥️ Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/MohammadrezaNarimaniUCDavis/TAE30-IoT-Lab-Materials.git
cd TAE30-IoT-Lab-Materials

# 2. Serve locally (Python 3)
python -m http.server 8000
# then visit http://localhost:8000 in your browser
```

_No dependencies are required—any static file server (or just opening `index.html`) will work._

---

## 🔧 Project Structure
```
├── index.html      # single‑page app
├── Images/         # course logos, instructor photos, lab diagrams
│   ├── Logos/
│   └── People/
└── README.md       # you’re reading it!
```

---

## 📚 Course Overview

The course introduces IoT fundamentals—sensors, actuators, wireless communication, cloud integration, edge computing, security, and data visualization—through ten progressive laboratory sessions. Each lab includes:

1. **Objectives & Required Materials**  
2. **Step‑by‑Step Tutorial** with circuit diagrams & block‑based / Arduino code  
3. **Additional Resources** for deeper exploration

---

## 🤝 Contributing

1. **Fork** the repository  
2. **Create** your feature branch (`git checkout -b feature/my-feature`)  
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)  
4. **Push** to the branch (`git push origin feature/my-feature`)  
5. **Open a Pull Request**

Please use the **Open Issue** button in the site header or the GitHub “Issues” tab for bugs or enhancement ideas.

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

## 🙏 Acknowledgements

* **UC Davis Biological & Agricultural Engineering** – course host  
* **Parallax BlocklyProp Solo** – block‑based programming environment  
* GitHub Pages – free static site hosting  
