#!/usr/bin/env python3
import json
import os
from pathlib import Path
from PIL import Image

base = Path(__file__).resolve().parent.parent
source_dir = base / 'images' / 'Gallery'
output_dir = base / 'images' / 'Gallery' / 'optimized'
output_dir.mkdir(exist_ok=True)

manifest_path = base / 'images' / 'gallery.json'
with manifest_path.open('r', encoding='utf-8') as fh:
    names = json.load(fh)

for name in names:
    src = source_dir / name
    if not src.exists():
        continue
    stem = src.stem
    ext = src.suffix.lower()
    if ext not in {'.webp', '.jpg', '.jpeg', '.png'}:
        continue

    try:
        with Image.open(src) as img:
            img = img.convert('RGB')
            max_dim = 320
            img.thumbnail((max_dim, max_dim), Image.Resampling.LANCZOS)
            out_path = output_dir / f'{stem}.webp'
            img.save(out_path, format='WEBP', quality=55, lossless=False)
    except Exception as exc:
        print(f'Failed {name}: {exc}')

print(f'Optimized {len(names)} images to {output_dir}')
