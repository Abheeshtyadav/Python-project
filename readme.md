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

Usage

Run the script:

python app.py

You’ll see a menu like:

==============================
Welcome, User
==============================
a. Set name
1. Basic QR Code
2. Custom QR Code
3. Exit
==============================
Select an option:

Basic QR Code

1. Choose option "1"
2. Enter the text/URL
3. Provide a filename (or press Enter for default "basic_qr.png")
4. The QR code will be saved

Custom QR Code

1. Choose option "2"
2. Enter the text/URL
3. Customize box size, border thickness, fill color, and background color
4. Provide a filename (or press Enter for default "custom_qr.png")
5. The QR code will be saved

Example

Select an option: 1
Enter the URL or text: https://github.com
Enter filename (default: basic_qr.png): github_qr
Saved to github_qr.png

Project Structure

project/
│
├── app.py          # Main script
├── README.md       # Documentation
└── qr_codes/       # (Optional) store generated QR codes

Notes

Filenames automatically append .png if missing.

Empty input for text/URL will cancel the operation.

Invalid numeric inputs for custom settings fall back to defaults.

License

This project is open‑source and free to use under the MIT License.