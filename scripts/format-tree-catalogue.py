#!/usr/bin/env python3
"""Format botanical names in tree-catalogue.html to match Excel/PDF conventions."""

import re
from pathlib import Path

root = Path(__file__).parent.parent
catalogue_file = root / "tree-catalogue.html"

def format_botanical_name(name):
    """
    Format botanical name:
    - Genus: capital
    - Species without variant: CAPITAL
    - Species with variant: lowercase, variant text kept as-is with proper case
    Examples: Acer Campestre (no variant), Acer campestre 'Red Shine' (with variant)
    """
    if not name or not isinstance(name, str):
        return name

    name = name.strip()

    # Use regex to match patterns like: GENUS species or GENUS species 'variant'
    # Handle both ' and &#39; for quotes
    variant_pattern = r"(.+?)\s+(['\&#;0-9]*)'?(.+?)'?\s*$|(.+?)\s+(['\&#;0-9]*)&#39;(.+?)&#39;\s*$"
    match = re.match(variant_pattern, name)

    if "'" in name or "&#39;" in name:
        # Has a variant
        if "&#39;" in name:
            # Extract using &#39;
            parts = name.split("&#39;")
            before = parts[0].strip()
            variant = parts[1] if len(parts) > 1 else ""
        else:
            # Extract using '
            parts = name.split("'")
            before = parts[0].strip()
            variant = parts[1] if len(parts) > 1 else ""

        before_parts = before.split()
        if len(before_parts) >= 2:
            genus = before_parts[0].capitalize()
            species = before_parts[1].lower()
            return f"{genus} {species} '{variant}'"
        elif len(before_parts) == 1:
            genus = before_parts[0].capitalize()
            return f"{genus} '{variant}'"
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


# Read the catalogue file
print(f"Reading tree catalogue: {catalogue_file}")
with open(catalogue_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace all botanical names in ci-latin spans
pattern = r'<p class="ci-latin">(.*?)</p>'
updated_count = 0

def replace_latin(match):
    global updated_count
    original = match.group(1)
    # Decode HTML entities temporarily for processing
    decoded = original.replace('&#39;', "'").replace('&#215;', '×')
    formatted = format_botanical_name(decoded)
    # Re-encode HTML entities for apostrophes
    encoded = formatted.replace("'", "&#39;").replace('×', '&#215;')

    if encoded != original:
        updated_count += 1
        if updated_count <= 50:  # Print first 50 changes
            print(f"  {original} → {encoded}")

    return f'<p class="ci-latin">{encoded}</p>'

content = re.sub(pattern, replace_latin, content)

# Write the updated content back
with open(catalogue_file, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n✓ Tree catalogue updated: {catalogue_file}")
print(f"  Botanical names formatted: {updated_count}")
