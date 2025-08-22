## Open-Redirect

<p align="left">
Open-Redirect is a tool for detecting open redirect vulnerabilities in web applications. These flaws allow attackers to redirect users to malicious sites using trusted URLs. This tool tests various parameters and payloads to identify unsafe redirects. Ideal for penetration testing and web security education.
</p>

<p align="center">
  <img src="https://github.com/denoyey/Open-Redirect/blob/b72c58e1731c6be449a621142c2bdb745e0d1208/Review-Tools.png" alt="Open-Redirect"/>
</p>

<div align="left">

![Build](https://img.shields.io/badge/build-stable-28a745?style=for-the-badge&logo=github)
![Platform](https://img.shields.io/badge/platform-Linux-0078D6?style=for-the-badge&logo=linux&logoColor=white)
![Last Commit](https://img.shields.io/github/last-commit/denoyey/Open-Redirect?style=for-the-badge&logo=git)
![Language](https://img.shields.io/github/languages/top/denoyey/Open-Redirect?style=for-the-badge&color=informational)
![Technologies](https://img.shields.io/badge/technologies-%20Python-yellow?style=for-the-badge&logo=terminal)
![Stars](https://img.shields.io/github/stars/denoyey/Open-Redirect?style=for-the-badge&color=ffac33&logo=github)
![Forks](https://img.shields.io/github/forks/denoyey/Open-Redirect?style=for-the-badge&color=blueviolet&logo=github)
![Issues](https://img.shields.io/github/issues/denoyey/Open-Redirect?style=for-the-badge&logo=github)
![Contributors](https://img.shields.io/github/contributors/denoyey/Open-Redirect?style=for-the-badge&color=9c27b0)

<br />

<img src="https://api.visitorbadge.io/api/VisitorHit?user=denoyey&repo=Open-Redirect&countColor=%237B1E7A&style=flat-square" alt="visitors"/>

</div>

## 🛠️ Features
- Multi-threaded scanning
- Supports scanning single URLs or URL lists
- Built-in payloads and redirect parameter list
- Custom headers and user-agents
- JSON and CSV export formats
- Simple, CLI-based interface

## 🖥️ Requirements
- Python **3.8+**
- Works on **Linux** and other
- Internet connection (to test redirects)

## 📦 Installation
```bash
git clone https://github.com/denoyey/Open-Redirect.git
cd Open-Redirect
pip install -r requirements.txt
```

## 🚀 Usage
Scan Single URL
```bash
python openredirect.py
```
> Choose option [1] and input the target URL when prompted.

Example:
```bash
https://example.com/redirect?url=
```

## 📄 Scan from File
Prepare a .txt file containing one URL per line, then:
```bash
python openredirect.py
```
> Choose option [2] and enter the file path when prompted.

## 🧪 Payloads & Parameters
- **Payloads**: Over 50 encoded and obfuscated redirect payloads are used to test for various bypass techniques.
- **Parameters**: Includes 60+ common redirect-related parameters like `url`, `redirect`, `next`, `target`, `dest`, and more.
> You can expand the list by modifying `bypass_payloads` and `redirect_params` in the script.

## 💾 Output Files
- `result.json` — JSON formatted scan results.
- `result.csv` — CSV formatted scan results.
- `log.txt` — Full scan log output.

## 🙌 Credits
Developed by <a href="https://github.com/denoyey">denoyey</a>.
Built for educational and ethical penetration testing purposes only.
Contributions and pull requests are welcome!
