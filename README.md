# 📄 QR Code Generator

A simple, fast web app that turns any URL into a downloadable QR code. Built with **Streamlit** and **qrcode**.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- 🔗 Paste or type any URL and instantly generate a QR code
- ⬇️ Download the QR code as a high-quality PNG
- 🎨 Auto-corrects missing `https://` prefixes
- 🧠 Runs entirely in memory — no files saved on the server
- 📱 Fully responsive — works great on mobile and desktop
- 🚀 Deployable for free on Streamlit Community Cloud

---

## 🖼️ Demo

Paste `example.com` → click **Generate QR Code** → download `example.png`.

*(Add a screenshot here once deployed: `![App Screenshot](screenshot.png)`)*

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Streamlit | Web UI |
| qrcode | QR code generation |
| Pillow | Image handling (PNG export) |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/qr-app.git
cd qr-app
```

### 2. Create and activate a virtual environment

Using `uv` (recommended, fast):

```bash
uv venv
# Windows
.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate
```

Using standard `venv`:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 📁 Project Structure

```
qr-app/
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
├── README.md            # You are here
└── .gitignore           # Files to ignore in Git
```

---

## 📦 Requirements

Create a `requirements.txt` with:

```txt
streamlit
qrcode[pil]
```

---

## 🧑‍💻 How It Works

1. **User input** — The user types a URL into the text box.
2. **Validation** — The app trims whitespace and prepends `https://` if missing.
3. **QR generation** — The `qrcode` library encodes the URL into a QR image.
4. **In-memory buffer** — The image is saved to a `BytesIO` object (not disk).
5. **Display + download** — Streamlit shows the image and provides a native download button.

No files touch the server's disk — everything is streamed to the browser on the fly.

---

## ☁️ Deployment (Streamlit Community Cloud)

1. Push your project to GitHub:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/qr-app.git
git push -u origin main
```

2. Go to [share.streamlit.io](https://share.streamlit.io) and click **New app**.
3. Select your repository, branch (`main`), and main file (`app.py`).
4. Click **Deploy**. Your app will be live at:

```
https://YOUR-USERNAME-qr-app.streamlit.app
```

---

## 🧪 Example Inputs

| Input | Result |
|---|---|
| `example.com` | Encodes `https://example.com` |
| `https://github.com` | Encodes as-is |
| `linkedin.com/in/username` | Encodes `https://linkedin.com/in/username` |

---

## 🗺️ Roadmap

- [ ] Color picker for QR foreground/background
- [ ] SVG download option (print-quality)
- [ ] Logo overlay in the center of the QR
- [ ] WiFi QR code support
- [ ] History of recently generated codes

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

1. Fork the repo
2. Create a branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m "Add amazing feature"`)
4. Push (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Onoriode Ofremu**

- GitHub: [@YOUR-USERNAME](https://github.com/onoriodeofremu)
- LinkedIn: [Endurance Onoriode Ofremu](https://linkedin.com)

---

## ⭐ Show Your Support

If this project helped you, give it a ⭐ on GitHub — it means a lot!

---

## 💡 Acknowledgements

- [Streamlit](https://streamlit.io) for the amazing framework
- [qrcode](https://pypi.org/project/qrcode/) for the QR generation logic
