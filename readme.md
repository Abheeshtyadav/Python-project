CLI QR Code Generator
A Python-based Command-Line Interface (CLI) tool for generating both standard and highly customized QR codes. Built for interactive terminal use, this generator allows you to easily create QR codes with custom sizes, border thicknesses, and colors, all with high error correction built-in.

Features
Interactive Menu Loop: Continues running until you explicitly choose to exit.

Basic Mode: Rapidly generate standard black-and-white QR codes.

Custom Mode: Customize box size, border thickness, fill color (names or hex codes), and background color.

High Error Correction (Level H): Automatically applies ERROR_CORRECT_H, ensuring the QR code remains scannable even if up to 30% of it is damaged, obscured, or covered by a central logo.

Dynamic Auto-Scaling: Automatically adjusts the internal QR code version matrix to fit the length of your input data.

Installation
This script requires Python 3.x and the qrcode library with Pillow support for image generation.

Clone or download this repository.

Install the required Python dependencies:

Bash
pip install "qrcode[pil]"
Usage
Run the script from your terminal:

Bash
python qr_generator.py
Example Workflow:

Select option 2 for a Custom QR Code.

Enter your URL (e.g., [https://github.com](https://github.com)).

Press Enter to use default sizing, or specify numbers for box size and border.

Enter colors (e.g., blue for fill, white for background).

Specify an output filename (e.g., github_qr.png).

The image will be saved directly in your current working directory.