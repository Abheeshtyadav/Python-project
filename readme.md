# QR Code Generator (Python)

A simple command‑line tool to generate QR codes in two modes:
- **Basic QR Code**: Quick generation with default settings.
- **Custom QR Code**: Allows customization of size, border, and colors.

---

## Features
- Generate QR codes from any text or URL.
- Save output as `.png` images.
- Customize:
  - Box size
  - Border thickness
  - Fill color
  - Background color
- Interactive menu with options to set your name, create QR codes, or exit.

---

## Requirements
- Python 3.x
- [qrcode](https://pypi.org/project/qrcode/) library

Install dependencies:
```bash
pip install qrcode[pil]
```

## Usage
- Run the script:

```bash
python app.py
```

You’ll see a menu like:
```text
==============================
Welcome, User
==============================
a. Set name
1. Basic QR Code
2. Custom QR Code
3. Exit
==============================
Select an option:
```