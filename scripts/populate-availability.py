#!/usr/bin/env python3
"""
Fetch tree products from Ecwid and populate availability-list-2026.xlsx

IMPORTANT REQUIREMENTS:
- Preserve existing column order: SKU, Botanical Name, Common Name, Pot Size, Height (cm), Girth (cm), Price (GBP), Stock
- Do NOT modify, reformat, or clean tree names — keep exactly as stored in Lightspeed/Ecwid
- Do NOT add or remove columns
- Tree names are the source of truth for botanical nomenclature — preserve all formatting, casing, special characters

Example: "ACACIA melanoxylon / Australian Blackwood" stays exactly as-is (do not split or transform)
"""

import os
import requests
import json
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment

STORE_ID = "73482057"
SECRET_TOKEN = os.getenv('ECWID_API_TOKEN')
if not SECRET_TOKEN:
    print("✗ Error: ECWID_API_TOKEN environment variable not set")
    exit(1)
BASE_URL = f"https://app.ecwid.com/api/v3/{STORE_ID}"

root = Path(__file__).parent.parent
from datetime import datetime
current_month = datetime.now().strftime('%B').lower()
xlsx_file = root / "files" / f"availability-list-{current_month}-2026.xlsx"

def fetch_products():
    """Fetch all products from Ecwid API."""
    headers = {"Authorization": f"Bearer {SECRET_TOKEN}"}
    products = []
    offset = 0
    limit = 100

    print("Fetching products from Ecwid...")

    while True:
        url = f"{BASE_URL}/products?offset={offset}&limit={limit}"
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code != 200:
            print(f"✗ API Error: {response.status_code}")
            print(f"Response: {response.text}")
            return None

        data = response.json()
        batch = data.get('items', [])

        if not batch:
            break

        products.extend(batch)
        offset += limit
        print(f"  Fetched {len(products)} products so far...")

    print(f"✓ Total products fetched: {len(products)}")
    return products

def create_availability_xlsx(products):
    """Create XLSX with exact product data from Ecwid.

    CRITICAL: Column order and names must match existing file structure.
    Tree names from Ecwid must be preserved exactly — no reformatting or modification.
    NOTE: Gift card and non-tree products are excluded. Data sorted by botanical name.
    """
    wb = Workbook()
    ws = wb.active
    ws.title = "Availability"

    # Header row with styling — DO NOT REORDER OR MODIFY THESE COLUMNS
    headers = ["SKU", "Botanical Name", "Common Name", "Pot Size", "Height (cm)", "Girth (cm)", "Price (GBP)", "Stock"]
    header_fill = PatternFill(start_color="334832", end_color="334832", fill_type="solid")
    header_font = Font(bold=True, color="FFFFFF", size=10)

    for col_idx, header in enumerate(headers, 1):
        cell = ws.cell(row=2, column=col_idx)
        cell.value = header
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="left", vertical="center")

    # Build data array, filter out gift cards and non-trees, then sort by botanical name
    data_rows = []

    for product in products:
        sku = product.get('sku', '').replace(' - Base', '')  # Remove " - Base" suffix
        full_name = product.get('name', '')  # Original from Ecwid

        # Split into botanical and common names
        parts = full_name.split(' / ')
        botanical = parts[0].strip() if parts else full_name
        common = parts[1].strip() if len(parts) > 1 else ""

        price = product.get('price', 0)

        # Calculate total quantity from combinations (variants)
        quantity = 0
        combinations = product.get('combinations', [])
        if combinations:
            quantity = sum(c.get('quantity', 0) for c in combinations)
        else:
            quantity = product.get('quantity', 0)

        # Extract pot size, height, and girth from attributes, combinations
        # NOTE: Remove zero/empty values (0, 0., 0 ) — leave blank if no valid measurement
        pot_size = ""
        height = ""
        girth = ""

        # Try product attributes first
        attributes = product.get('attributes', [])
        for attr in attributes:
            attr_name = attr.get('name', '').lower()
            attr_value = attr.get('value', '')
            if 'pot' in attr_name:
                pot_size = attr_value
            elif 'height' in attr_name:
                height = attr_value
            elif 'girth' in attr_name or 'circumference' in attr_name:
                girth = attr_value

        # Try combination options if no data found yet
        if (not pot_size or not height or not girth) and combinations:
            for combo in combinations:
                options = combo.get('options', [])
                for opt in options:
                    opt_name = opt.get('name', '').lower()
                    opt_value = opt.get('value', '')
                    if 'pot' in opt_name and not pot_size:
                        pot_size = opt_value
                    elif 'height' in opt_name and not height:
                        height = opt_value
                    elif ('girth' in opt_name or 'circumference' in opt_name) and not girth:
                        girth = opt_value

        # Clean up invalid girth/height data
        # NOTE: Remove patterns: 0, 0., 0 , '0, 0', 0', - 0, and other zero-only values
        # Keep valid formats like: 50 - 75, 8/10, 200 - 225, etc.
        for val_var in [('height', height), ('girth', girth)]:
            val_name, val = val_var
            if val:
                val_str = str(val).strip()
                # Check for invalid patterns: zero with quotes (0', '0), dash-zero (- 0, -0, etc.), etc.
                invalid_patterns = ["0'", "'0", '0"', '"0', "- 0", "-0", "0 -"]
                if any(pattern in val_str for pattern in invalid_patterns) or val_str.endswith("- 0"):
                    if val_name == 'height':
                        height = ""
                    else:
                        girth = ""
                else:
                    # Remove quotes and trailing dots for comparison
                    val_clean = val_str.strip("'\"").rstrip('.')
                    # Only remove if it's just a zero (with or without quotes/dots)
                    if val_clean == '0' or val_clean == '' or not val_clean:
                        if val_name == 'height':
                            height = ""
                        else:
                            girth = ""

        # Skip gift cards, non-tree products, and zero stock items
        if (sku and 'gift' not in sku.lower() and 'gift' not in full_name.lower()
            and quantity > 0):  # Only include items with stock

            # Format height and girth with better spacing, remove "cm", trim spaces
            # Apply rules: remove leading/trailing spaces and invalid patterns
            formatted_height = height
            if height:
                formatted_height = str(height).lower().replace('cm', '').replace('-', ' - ').replace('  ', ' ').strip()
                # Apply cleanup rules after formatting
                if any(pat in formatted_height for pat in ["0'", "'0", '0"', '"0', "- 0", "-0"]):
                    formatted_height = ""

            formatted_girth = girth
            if girth:
                formatted_girth = str(girth).lower().replace('cm', '').replace('-', ' - ').replace('  ', ' ').strip()
                # Apply cleanup rules after formatting: remove .0, .), 0', etc.
                if any(pat in formatted_girth for pat in ["0'", "'0", '0"', '"0', "- 0", "-0", ".0", ".)"]):
                    formatted_girth = ""

            data_rows.append({
                'sku': sku,
                'botanical': botanical,
                'common': common,
                'pot_size': pot_size,
                'height': formatted_height,
                'girth': formatted_girth,
                'price': price,
                'quantity': quantity,
            })

    # Sort by botanical name
    data_rows.sort(key=lambda x: (x['botanical'] or '').lower())

    # Write sorted rows to XLSX
    row_idx = 3
    for row_data in data_rows:
        ws.cell(row=row_idx, column=1).value = row_data['sku']
        ws.cell(row=row_idx, column=2).value = row_data['botanical']
        ws.cell(row=row_idx, column=3).value = row_data['common']
        ws.cell(row=row_idx, column=4).value = row_data['pot_size']
        ws.cell(row=row_idx, column=5).value = row_data['height']
        ws.cell(row=row_idx, column=6).value = row_data['girth']
        ws.cell(row=row_idx, column=7).value = row_data['price']
        ws.cell(row=row_idx, column=8).value = row_data['quantity']
        row_idx += 1

    # Adjust column widths
    ws.column_dimensions['A'].width = 12  # SKU
    ws.column_dimensions['B'].width = 25  # Botanical Name
    ws.column_dimensions['C'].width = 25  # Common Name
    ws.column_dimensions['D'].width = 12  # Pot Size
    ws.column_dimensions['E'].width = 12  # Height (cm)
    ws.column_dimensions['F'].width = 12  # Girth (cm)
    ws.column_dimensions['G'].width = 12  # Price (GBP)
    ws.column_dimensions['H'].width = 10  # Stock

    # Save
    wb.save(str(xlsx_file))
    print(f"✓ XLSX created: {xlsx_file}")
    print(f"  Total rows: {row_idx - 3}")

    return row_idx - 3

def main():
    """Main flow."""
    print("=" * 60)
    print("Papervale Trees — Populate Availability List")
    print("=" * 60 + "\n")

    # Fetch products
    products = fetch_products()
    if not products:
        print("✗ Failed to fetch products")
        return False

    # Create XLSX
    count = create_availability_xlsx(products)

    print("\n" + "=" * 60)
    print("✓ Next step: Run generate-availability.py to create PDF")
    print("=" * 60)

    return True

if __name__ == "__main__":
    try:
        success = main()
        exit(0 if success else 1)
    except Exception as e:
        print(f"✗ Error: {e}")
        exit(1)
