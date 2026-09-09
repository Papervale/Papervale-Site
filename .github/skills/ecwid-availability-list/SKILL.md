---
name: ecwid-availability-list
description: 'Refresh Papervale Trees availability files from the Ecwid API. Use when generating or updating the seasonal availability XLSX and PDF, fetching latest stock, preserving the existing ordering/grouping, or checking availability-list output.'
argument-hint: '[season or month, for example September 2026]'
user-invocable: true
---

# Ecwid Availability List

Refresh the Papervale Trees stock list from Ecwid and produce the matching Excel and PDF files in `files/`.

## When to Use

- The user asks for the latest Ecwid stock or availability list.
- The seasonal XLSX or PDF needs to be regenerated.
- The output must match the current workbook's format, ordering, and grouping.

## Procedure

1. Confirm the requested month and year. The existing scripts derive the month from the current date and currently target the 2026 seasonal filenames.
2. Confirm `.env` contains `ECWID_SECRET_TOKEN`. Never print or expose the token.
3. Run the read-only Ecwid refresh and workbook generator from the repository root:

   ```sh
   ./.venv/bin/python scripts/populate-availability.py
   ```

   This fetches all product pages from store `73482057`, excludes gift cards, keeps only combinations with quantity greater than zero, and writes the nine-column workbook format.

4. Generate the PDF from the refreshed workbook:

   ```sh
   ./.venv/bin/python scripts/generate-availability.py
   ```

5. Validate the output files in `files/availability-list-<month>-2026.xlsx` and `files/availability-list-<month>-2026.pdf`.

## Output Contract

Preserve these columns and order:

`SKU`, `Botanical Name`, `Common Name`, `Pot Size`, `Height (cm)`, `Girth (cm)`, `Price (inc. vat)`, `Stock`, `Order`

The workbook data begins on row 5. Preserve Ecwid tree names and the established sort order: botanical name, then numeric pot-size value, then numeric girth value. Do not manually reorder rows, rename columns, or alter the blank `Order` column. The PDF is generated from the workbook and must report the same stock-line count.

## Safety and Troubleshooting

- Use only `GET` requests through the existing Python script. Never modify Ecwid products, inventory, or orders.
- If authentication fails, stop and report the API status without exposing credentials.
- If the API returns no products or the generator produces zero rows, do not replace a valid existing output.
- If PDF text extraction utilities are unavailable, validate the PDF by checking that it exists, has a non-zero size, and was generated after the workbook.
- Report the fetched product count, output row count, output paths, and validation result.

## Repository Resources

- [Ecwid refresh and XLSX generator](../../../scripts/populate-availability.py)
- [XLSX-to-PDF generator](../../../scripts/generate-availability.py)
- [Ecwid configuration reference](../../../docs/ECWID.md)
