# QR Code Generator

A simple Python project that generates QR codes from user input and saves them as PNG images.

## Features

- Takes text or a URL as input
- Generates a QR code image
- Saves the image as a `.png` file
- Automatically adds `.png` if the extension is missing

## Requirements

- Python 3.x
- `qrcode`
- `Pillow`

## Installation

Create and activate a virtual environment, then install the required packages.

```bash
pip install qrcode pillow
```

## How to Run

Run the Python file:

```bash
python qr_code_generator.py
```

Then enter:

- The text or URL you want to convert into a QR code
- The file name you want to save

## Example

```text
Enter URL: https://example.com
Enter file name: my_qr
```

This will save the file as:

```text
my_qr.png
```

## Project File

- `qr_code_generator.py` → main Python script

## Notes

This project uses the `qrcode` library to generate QR codes. It also needs `Pillow` because the image output depends on the `PIL` module.

