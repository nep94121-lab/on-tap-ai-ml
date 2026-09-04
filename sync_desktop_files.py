#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sync_desktop_files.py
Sao chép đồng bộ 100% index.html sang 2 file đích trên Desktop và xác thực SHA256.
"""

import hashlib
import os
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_HTML = os.path.join(BASE_DIR, "index.html")

DEST_FILES = [
    r"C:\Users\Admin\Desktop\học tập\on_tap_ai_ml.html",
    r"C:\Users\Admin\Desktop\on_tap_ai_ml.html"
]

def get_sha256(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

def sync():
    src_hash = get_sha256(SRC_HTML)
    src_size = os.path.getsize(SRC_HTML)
    print(f"[*] File nguồn: {SRC_HTML}")
    print(f"    - Kích thước: {src_size} bytes")
    print(f"    - SHA256: {src_hash}")

    for dest in DEST_FILES:
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copy2(SRC_HTML, dest)
        dest_hash = get_sha256(dest)
        dest_size = os.path.getsize(dest)
        print(f"[+] Đã sao chép sang: {dest}")
        print(f"    - Kích thước: {dest_size} bytes")
        print(f"    - SHA256: {dest_hash}")
        assert src_hash == dest_hash, f"LỖI ĐỒNG BỘ: SHA256 không khớp tại {dest}!"

    print("\n🎉 THÀNH CÔNG: Cả 3 file HTML đã được đồng bộ 100% đồng nhất SHA256!")

if __name__ == "__main__":
    sync()
