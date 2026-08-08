#!/usr/bin/env python3
"""Format botanical names in all tree detail pages to match Excel/PDF conventions."""

import re
from pathlib import Path

root = Path(__file__).parent.parent
trees_dir = root / "trees"

def format_botanical_name(name):
    """
    Format botanical name:
    - Genus: capital
    - Species without variant: CAPITAL
    - Species with variant: lowercase, variant text kept as-is
    Examples: Acer Campestre (no variant), Acer campestre 'Red Shine' (with variant)
    """
    if not name or not isinstance(name, str):
        return name

    name = name.strip()

    # Check if name contains a variant (quoted text) - handle regular, smart, and HTML quotes
    # U+2018=left, U+2019=right smart quotes
    left_smart = chr(0x2018)
    right_smart = chr(0x2019)

    has_variant = ("’" in name or "&#39;" in name or left_smart in name or right_smart in name)

    if has_variant:
        # Has a variant - extract the part before the quote and the variant text
        before = None
        variant = None

        if "&#39;" in name:
            parts = name.split("&#39;")
            before = parts[0].strip()
            variant = parts[1] if len(parts) > 1 else ""
        elif left_smart in name and right_smart in name:
            # Smart quotes - extract between them
            start = name.find(left_smart)
            end = name.find(right_smart)
            if start >= 0 and end > start:
                before = name[:start].strip()
                variant = name[start+1:end]
        elif right_smart in name:
            # Only right smart quote
            parts = name.rsplit(right_smart, 1)
            before = parts[0].strip()
            variant = ""
        elif left_smart in name:
            # Only left smart quote
            parts = name.split(left_smart)
            before = parts[0].strip()
            variant = parts[1] if len(parts) > 1 else ""
        elif "’" in name:  # Regular single quote
            parts = name.split("’")
            before = parts[0].strip()
            variant = parts[1] if len(parts) > 1 else ""

        if before and variant is not None:
            before_parts = before.split()
            if len(before_parts) >= 2:
                genus = before_parts[0].capitalize()
                species = before_parts[1].lower()
                return f"{genus} {species} ‘{variant}’"
            elif len(before_parts) == 1:
                genus = before_parts[0].capitalize()
                return f"{genus} ‘{variant}’"
    else:
        # No variant
        parts = name.split()
        if len(parts) >= 2:
            genus = parts[0].lower() if parts[0].lower() == 'x' else parts[0].capitalize()
            species = parts[1].capitalize()
            rest = ' '.join(parts[2:])
            if rest:
                return f"{genus} {species} {rest}"
            return f"{genus} {species}"
        elif len(parts) == 1:
            return parts[0].capitalize()

    return name


# Find all tree HTML files
tree_files = list(trees_dir.glob("*.html"))
print(f"Found {len(tree_files)} tree pages")

total_updated = 0

for tree_file in sorted(tree_files):
    with open(tree_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find and replace botanical names in product-latin spans
    pattern = r'<p class="product-latin">(.*?)</p>'

    def replace_latin(match):
        original = match.group(1)
        # Decode HTML entities temporarily for processing
        decoded = original.replace('&#39;', "'").replace('&#215;', '×')
        formatted = format_botanical_name(decoded)
        # Re-encode HTML entities for apostrophes
        encoded = formatted.replace("'", "&#39;").replace('×', '&#215;')

        return f'<p class="product-latin">{encoded}</p>'

    new_content = re.sub(pattern, replace_latin, content)

    if new_content != content:
        with open(tree_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        total_updated += 1
        print(f"  {tree_file.name}: updated")

print(f"\n✓ All tree pages updated")
print(f"  Total botanical names formatted: {total_updated}")
