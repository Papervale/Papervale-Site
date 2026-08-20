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

import requests
import json
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment

STORE_ID = "73482057"
SECRET_TOKEN = "secret_CydqzttNqkyKHwie7NUEWsQvjTCFzykc"
BASE_URL = f"https://app.ecwid.com/api/v3/{STORE_ID}"

root = Path(__file__).parent.parent
xlsx_file = root / "files" / "availability-list-2026.xlsx"

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

    # Populate data rows
    row_idx = 3
    for product in products:
        sku = product.get('sku', '')
        name = product.get('name', '')  # PRESERVE EXACTLY AS STORED IN LIGHTSPEED
        price = product.get('price', 0)
        quantity = product.get('quantity', 0)

        # Parse product name for botanical and common names
        # Example format: "ACACIA melanoxylon / Australian Blackwood"
        # Keep exact formatting from Ecwid — do NOT modify casing, special chars, or spacing
        parts = name.split(' / ')
        if len(parts) >= 2:
            botanical = parts[0].strip()  # e.g., "ACACIA melanoxylon"
            common = ' / '.join(parts[1:]).strip()  # e.g., "Australian Blackwood"
        else:
            botanical = name
            common = ""

        # Get custom fields if available (pot size, height, girth)
        attributes = product.get('attributes', [])
        pot_size = ""
        height = ""
        girth = ""

        for attr in attributes:
            attr_name = attr.get('name', '').lower()
            attr_value = attr.get('value', '')
            if 'pot' in attr_name:
                pot_size = attr_value
            elif 'height' in attr_name:
                height = attr_value
            elif 'girth' in attr_name or 'circumference' in attr_name:
                girth = attr_value

        # Write row
        ws.cell(row=row_idx, column=1).value = sku
        ws.cell(row=row_idx, column=2).value = botanical
        ws.cell(row=row_idx, column=3).value = common
        ws.cell(row=row_idx, column=4).value = pot_size
        ws.cell(row=row_idx, column=5).value = height
        ws.cell(row=row_idx, column=6).value = girth
        ws.cell(row=row_idx, column=7).value = price
        ws.cell(row=row_idx, column=8).value = quantity

        row_idx += 1

    # Adjust column widths
    ws.column_dimensions['A'].width = 12
    ws.column_dimensions['B'].width = 25
    ws.column_dimensions['C'].width = 25
    ws.column_dimensions['D'].width = 12
    ws.column_dimensions['E'].width = 15
    ws.column_dimensions['F'].width = 15
    ws.column_dimensions['G'].width = 12
    ws.column_dimensions['H'].width = 10

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
