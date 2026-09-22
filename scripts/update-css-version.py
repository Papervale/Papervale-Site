#!/usr/bin/env python3
"""
Auto-update CSS version hash in all HTML files.
Generates an MD5 hash of styles.css and updates ?v=HASH in all HTML files.
Run before deployment to cache-bust CSS changes.
"""

import hashlib
import re
from pathlib import Path

root = Path(__file__).parent.parent
css_file = root / "styles.css"
html_files = list(root.glob("*.html"))

def get_css_hash():
    """Generate MD5 hash of CSS file."""
    with open(css_file, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()[:7]  # Use first 7 chars

def update_html_files(new_version):
    """Update CSS version in all HTML files."""
    pattern = r'href="styles\.css\?v=[a-f0-9]+"'
    replacement = f'href="styles.css?v={new_version}"'

    updated_count = 0
    for html_file in html_files:
        with open(html_file, 'r') as f:
            content = f.read()

        if 'styles.css' in content:
            updated_content = re.sub(pattern, replacement, content)
            if updated_content != content:
                with open(html_file, 'w') as f:
                    f.write(updated_content)
                print(f"✓ {html_file.name}")
                updated_count += 1

    return updated_count

def main():
    print("=" * 60)
    print("CSS Version Hash Generator")
    print("=" * 60 + "\n")

    new_version = get_css_hash()
    print(f"CSS file hash: {new_version}\n")
    print(f"Updating {len(html_files)} HTML files...\n")

    updated = update_html_files(new_version)

    print(f"\n✓ Updated {updated} file(s)")
    print(f"  Next deployment will cache-bust all CSS changes automatically")

if __name__ == "__main__":
    main()
