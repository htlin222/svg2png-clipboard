#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# title: svg_to_png_clipboard
# author: Hsieh-Ting Lin, the Lizard 🦎
# description: svg_to_png_clipboard is a script about...
# date: "2025-07-02"
# --END--
import os
import subprocess
import tempfile
from xml.etree import ElementTree as ET

import pyperclipimg as pci

IMG_SIZE = 180


def get_clipboard_text():
    return subprocess.run("pbpaste", text=True, capture_output=True).stdout


def is_valid_svg(text):
    try:
        root = ET.fromstring(text)
        return root.tag.endswith("svg")
    except ET.ParseError:
        return False


def write_svg(svg):
    f = tempfile.NamedTemporaryFile(delete=False, suffix=".svg")
    f.write(svg.encode("utf-8"))
    f.close()
    return f.name


def svg_to_png(svg_path, png_path, size=IMG_SIZE):
    subprocess.run(
        ["rsvg-convert", "-w", str(size), "-h", str(size), "-o", png_path, svg_path],
        check=True,
    )


def main():
    svg = get_clipboard_text()
    if not is_valid_svg(svg):
        print("❌ Clipboard does not contain valid SVG.")
        return

    svg_file = write_svg(svg)
    png_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png").name

    try:
        svg_to_png(svg_file, png_file, size=IMG_SIZE)
        pci.copy(png_file)  # ✅ Copies correct image/png blob
        print(f"✅ PNG ({IMG_SIZE}×{IMG_SIZE}) copied to clipboard.")
        # Display macOS notification
        subprocess.run([
            "osascript", "-e",
            'display notification "Image successfully copied to clipboard." with title "SVG to PNG"'
        ])
        print("📣 Notification sent: Image successfully copied to clipboard.")
    finally:
        os.remove(svg_file)
        os.remove(png_file)


if __name__ == "__main__":
    main()
