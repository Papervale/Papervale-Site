#!/usr/bin/env python3
"""
Optimize gallery images: compress, resize, convert to WebP, and update HTML.

Creates responsive image variants:
- Thumbnail (300px): for masonry grid
- Medium (1200px): for lightbox
- Full: compressed original
- All with WebP + JPEG fallback
"""

import os
from pathlib import Path
from PIL import Image
import json
import re

root = Path(__file__).parent.parent
gallery_dir = root / "assets" / "images" / "gallery"
optimized_dir = root / "assets" / "images" / "gallery-optimized"
gallery_html = root / "gallery.html"

# Create optimized directory
optimized_dir.mkdir(parents=True, exist_ok=True)

# Image dimensions for variants
SIZES = {
    'thumb': 300,      # For masonry
    'medium': 1200,    # For lightbox
}

def get_image_files():
    """Get all gallery images excluding optimized versions."""
    exts = {'.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG'}
    files = [f for f in gallery_dir.iterdir() if f.suffix in exts]
    return sorted(files)

def optimize_image(src_path, basename):
    """Create thumbnail, medium, and full variants in WebP and JPEG."""
    try:
        img = Image.open(src_path)

        # Ensure RGB for JPEG
        if img.mode in ('RGBA', 'LA', 'P'):
            bg = Image.new('RGB', img.size, (255, 255, 255))
            bg.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
            img = bg
        elif img.mode != 'RGB':
            img = img.convert('RGB')

        original_width = img.width
        original_height = img.height

        variants = {}

        # Thumbnail (300px)
        thumb_width = min(SIZES['thumb'], original_width)
        thumb_height = int((thumb_width / original_width) * original_height)
        thumb = img.resize((thumb_width, thumb_height), Image.Resampling.LANCZOS)

        thumb_jpg = optimized_dir / f"{basename}-thumb.jpg"
        thumb_webp = optimized_dir / f"{basename}-thumb.webp"
        thumb.save(thumb_jpg, 'JPEG', quality=75, optimize=True)
        thumb.save(thumb_webp, 'WEBP', quality=75)
        variants['thumb'] = {
            'jpg': thumb_jpg.name,
            'webp': thumb_webp.name,
            'size': f"{thumb_width}px"
        }

        # Medium (1200px)
        medium_width = min(SIZES['medium'], original_width)
        medium_height = int((medium_width / original_width) * original_height)
        medium = img.resize((medium_width, medium_height), Image.Resampling.LANCZOS)

        medium_jpg = optimized_dir / f"{basename}-medium.jpg"
        medium_webp = optimized_dir / f"{basename}-medium.webp"
        medium.save(medium_jpg, 'JPEG', quality=80, optimize=True)
        medium.save(medium_webp, 'WEBP', quality=80)
        variants['medium'] = {
            'jpg': medium_jpg.name,
            'webp': medium_webp.name,
            'size': f"{medium_width}px"
        }

        # Full (compressed original)
        full_jpg = optimized_dir / f"{basename}-full.jpg"
        full_webp = optimized_dir / f"{basename}-full.webp"
        img.save(full_jpg, 'JPEG', quality=85, optimize=True)
        img.save(full_webp, 'WEBP', quality=85)
        variants['full'] = {
            'jpg': full_jpg.name,
            'webp': full_webp.name,
            'size': f"{original_width}px"
        }

        # Get file sizes
        sizes = {
            k: {
                **v,
                'jpg_size': full_jpg.stat().st_size if k == 'full' else 0,
                'webp_size': full_webp.stat().st_size if k == 'full' else 0,
            }
            for k, v in variants.items()
        }

        orig_size = src_path.stat().st_size
        compressed_size = (optimized_dir / f"{basename}-thumb.jpg").stat().st_size + \
                         (optimized_dir / f"{basename}-medium.jpg").stat().st_size + \
                         (optimized_dir / f"{basename}-full.jpg").stat().st_size + \
                         (optimized_dir / f"{basename}-thumb.webp").stat().st_size + \
                         (optimized_dir / f"{basename}-medium.webp").stat().st_size + \
                         (optimized_dir / f"{basename}-full.webp").stat().st_size

        compression = (1 - compressed_size / orig_size) * 100 if orig_size > 0 else 0

        print(f"✓ {src_path.name:40} {orig_size/1024/1024:5.1f}MB → {compressed_size/1024/1024:5.1f}MB ({compression:5.0f}%)")

        return variants
    except Exception as e:
        print(f"✗ Error processing {src_path.name}: {e}")
        return None

def build_responsive_img(basename, variants, alt_text):
    """Build responsive <picture> HTML with WebP and JPEG."""
    result = '<picture>\n'

    # WebP sources
    result += f'      <source srcset="assets/images/gallery-optimized/{variants["thumb"]["webp"]} 300w, '
    result += f'assets/images/gallery-optimized/{variants["medium"]["webp"]} 1200w, '
    result += f'assets/images/gallery-optimized/{variants["full"]["webp"]} {variants["full"]["size"]}" '
    result += 'type="image/webp">\n'

    # JPEG fallback
    result += f'      <source srcset="assets/images/gallery-optimized/{variants["thumb"]["jpg"]} 300w, '
    result += f'assets/images/gallery-optimized/{variants["medium"]["jpg"]} 1200w, '
    result += f'assets/images/gallery-optimized/{variants["full"]["jpg"]} {variants["full"]["size"]}" '
    result += 'type="image/jpeg">\n'

    # Fallback img (used if picture not supported, and what gets displayed)
    result += f'      <img src="assets/images/gallery-optimized/{variants["medium"]["jpg"]}" '
    result += f'alt="{alt_text}" loading="lazy">'
    result += '\n    </picture>'

    return result

def update_gallery_html(image_data):
    """Update gallery.html with responsive images."""
    with open(gallery_html, 'r') as f:
        content = f.read()

    # Find all masonry-item divs and replace img tags
    pattern = r'<div class="masonry-item" data-index="(\d+)">\s*<img src="([^"]+)" alt="([^"]*)"[^>]*loading="lazy">'

    def replace_img(match):
        index = int(match.group(1))
        src = match.group(2)
        alt = match.group(3)

        # Extract basename from path
        filename = Path(src).name
        basename = Path(filename).stem

        # Find matching image data
        for img_path, variants in image_data.items():
            if Path(img_path).stem == basename:
                responsive = build_responsive_img(basename, variants, alt)
                return f'<div class="masonry-item" data-index="{index}">\n    {responsive}\n      <div class="masonry-item-overlay">'

        # If not found, return original
        return match.group(0)

    updated = re.sub(pattern, replace_img, content)

    with open(gallery_html, 'w') as f:
        f.write(updated)

    print(f"\n✓ Updated {gallery_html.name}")

def main():
    print("=" * 80)
    print("Papervale Gallery Image Optimizer")
    print("=" * 80 + "\n")

    files = get_image_files()
    print(f"Found {len(files)} gallery images\n")

    if not files:
        print("No images found in gallery folder")
        return

    image_data = {}
    total_before = 0
    total_after = 0

    for src_path in files:
        basename = src_path.stem
        variants = optimize_image(src_path, basename)

        if variants:
            image_data[str(src_path)] = variants
            total_before += src_path.stat().st_size

            # Sum all variant sizes
            for size_key in ['thumb', 'medium', 'full']:
                if f"{basename}-{size_key}.jpg" in str(optimized_dir):
                    jpg_path = optimized_dir / f"{basename}-{size_key}.jpg"
                    webp_path = optimized_dir / f"{basename}-{size_key}.webp"
                    if jpg_path.exists():
                        total_after += jpg_path.stat().st_size
                    if webp_path.exists():
                        total_after += webp_path.stat().st_size

    print("\n" + "=" * 80)
    print("Summary:")
    print(f"  Original size:  {total_before / 1024 / 1024:.1f} MB")
    print(f"  Optimized size: {total_after / 1024 / 1024:.1f} MB")
    print(f"  Total savings:  {(1 - total_after / total_before) * 100:.0f}%")
    print("=" * 80)

    # Update HTML with responsive images
    if image_data:
        update_gallery_html(image_data)
        print("\n✓ Gallery optimization complete!")
        print("  • Images optimized to WebP + JPEG")
        print("  • HTML updated with responsive <picture> tags")
        print("  • Serving smallest variant needed for each device")
    else:
        print("✗ No images were processed")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
