# generate-availability.ps1
# Generates files/availability-list-2026.xlsx from Ecwid product data.
# Run from the repo root:  pwsh scripts/generate-availability.ps1
#
# To fetch FRESH data from Ecwid before generating, set $EcwidToken below.
# Leave it empty to use the cached ecwid-products.json.

param(
    [string]$EcwidToken = ''
)

$root    = $PSScriptRoot | Split-Path -Parent
$outDir  = "$root\files"
$storeId = '73482057'

if (-not (Test-Path $outDir)) { New-Item -ItemType Directory -Path $outDir -Force | Out-Null }

# ── 1. Optionally refresh product cache from Ecwid API ───────────────────────
if ($EcwidToken) {
    Write-Host 'Fetching products from Ecwid API...'
    $allProds = [System.Collections.Generic.List[object]]::new()
    $offset   = 0
    do {
        $uri = "https://app.ecwid.com/api/v3/$storeId/products?limit=100&offset=$offset&enabled=true"
        $r   = Invoke-RestMethod -Uri $uri -Headers @{ Authorization = "Bearer $EcwidToken" }
        $allProds.AddRange($r.items)
        $offset += 100
        Write-Host "  Fetched $($allProds.Count) / $($r.total)"
    } while ($allProds.Count -lt $r.total)

    $allProds | ConvertTo-Json -Depth 20 | Set-Content "$root\ecwid-products.json" -Encoding UTF8
    Write-Host "Cache updated: ecwid-products.json ($($allProds.Count) products)"
} else {
    Write-Host 'Using cached ecwid-products.json (pass -EcwidToken to refresh from API)'
}

# ── 2. Load data ──────────────────────────────────────────────────────────────
$products = Get-Content "$root\ecwid-products.json" -Raw | ConvertFrom-Json

# ── 3. Build rows ─────────────────────────────────────────────────────────────
$rows = [System.Collections.Generic.List[PSCustomObject]]::new()

foreach ($p in $products) {
    if (-not $p.enabled) { continue }

    $parts      = $p.name -split ' / ', 2
    $latinRaw   = $parts[0].Trim()
    $commonName = if ($parts.Count -gt 1) { $parts[1].Trim() } else { '' }
    $latinName  = (Get-Culture).TextInfo.ToTitleCase($latinRaw.ToLower())

    if ($p.combinations -and $p.combinations.Count -gt 0) {
        foreach ($c in $p.combinations) {
            if (-not $c.inStock -and $p.outOfStockVisibilityBehaviour -eq 'HIDE') { continue }

            $potSize = ($c.options | Where-Object { $_.name -eq 'Pot Size' }    | Select-Object -First 1).value
            $height  = ($c.options | Where-Object { $_.name -eq 'Height (cm)' } | Select-Object -First 1).value
            $qty     = if ($c.unlimited) { 'Unlimited' } elseif (-not $c.inStock) { 'Out of Stock' } else { [string]$c.quantity }

            $rows.Add([PSCustomObject]@{
                'Botanical Name' = $latinName
                'Common Name'    = $commonName
                'Pot Size'       = $potSize
                'Height (cm)'    = $height
                'Price (GBP)'    = $c.defaultDisplayedPrice
                'Stock'          = $qty
                'SKU'            = $c.sku
            })
        }
    } else {
        $potSize = ($p.options | Where-Object { $_.name -eq 'Pot Size' }    | Select-Object -First 1).choices[0].text
        $height  = ($p.options | Where-Object { $_.name -eq 'Height (cm)' } | Select-Object -First 1).choices[0].text
        $qty     = if ($p.unlimited) { 'Unlimited' } elseif (-not $p.inStock) { 'Out of Stock' } else { [string]$p.quantity }

        $rows.Add([PSCustomObject]@{
            'Botanical Name' = $latinName
            'Common Name'    = $commonName
            'Pot Size'       = $potSize
            'Height (cm)'    = $height
            'Price (GBP)'    = $p.price
            'Stock'          = $qty
            'SKU'            = $p.sku
        })
    }
}

$sorted = $rows | Sort-Object 'Botanical Name', 'Height (cm)', 'Pot Size'
Write-Host "Rows: $($sorted.Count)"

# ── 4. Export Excel ───────────────────────────────────────────────────────────
$outFile = "$outDir\availability-list-2026.xlsx"

$xlPkg = $sorted | Export-Excel -Path $outFile -WorksheetName 'Availability' `
    -TableName 'AvailabilityList' -TableStyle Medium7 `
    -AutoSize -FreezeTopRow -AutoFilter `
    -Title 'Papervale Trees — Availability List 2026' `
    -TitleBold -TitleSize 14 `
    -PassThru

$ws      = $xlPkg.Workbook.Worksheets['Availability']
$lastRow = $ws.Dimension.End.Row
$greenBg = [System.Drawing.Color]::FromArgb(234, 242, 234)
$greenFg = [System.Drawing.Color]::FromArgb(30, 90, 30)
$redBg   = [System.Drawing.Color]::FromArgb(253, 237, 234)
$redFg   = [System.Drawing.Color]::FromArgb(180, 60, 40)

for ($r = 3; $r -le $lastRow; $r++) {
    $cell = $ws.Cells[$r, 6]
    $val  = $cell.Text
    if ($val -eq 'Out of Stock') {
        $cell.Style.Font.Color.SetColor($redFg)
        $cell.Style.Fill.PatternType = [OfficeOpenXml.Style.ExcelFillStyle]::Solid
        $cell.Style.Fill.BackgroundColor.SetColor($redBg)
    } elseif ($val -ne '') {
        $cell.Style.Font.Color.SetColor($greenFg)
        $cell.Style.Fill.PatternType = [OfficeOpenXml.Style.ExcelFillStyle]::Solid
        $cell.Style.Fill.BackgroundColor.SetColor($greenBg)
    }
}

Close-ExcelPackage $xlPkg
Write-Host "Generated: $outFile"

# ── 5. Generate PDF via Edge headless ────────────────────────────────────────
$edge = @(
    'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
    'C:\Program Files\Microsoft\Edge\Application\msedge.exe'
) | Where-Object { Test-Path $_ } | Select-Object -First 1

if ($edge) {
    # Build HTML table
    $tableRows = $sorted | ForEach-Object {
        $stockClass = if ($_.Stock -eq 'Out of Stock') { ' oos' } else { ' ins' }
        $price = if ($_.'Price (GBP)') { [string]::Format('£{0:N2}', $_.'Price (GBP)') } else { '' }
        "<tr><td>$($_.'Botanical Name')</td><td>$($_.'Common Name')</td><td>$($_.'Pot Size')</td><td>$($_.'Height (cm)')</td><td class=price>$price</td><td class='stock$stockClass'>$($_.'Stock')</td><td>$($_.'SKU')</td></tr>"
    }
    $date = Get-Date -Format 'MMMM yyyy'
    $html = @"
<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<title>Papervale Trees — Availability List 2026</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:'Segoe UI',Arial,sans-serif;font-size:9pt;color:#1a1a1a}
.header{padding:16px 20px 12px;border-bottom:2px solid #334832;margin-bottom:12px;display:flex;justify-content:space-between;align-items:flex-end}
.header h1{font-size:16pt;font-weight:600;color:#334832}.header p{font-size:8pt;color:#666;margin-top:2px}.meta{font-size:8pt;color:#666;text-align:right}
table{width:100%;border-collapse:collapse}
thead th{background:#334832;color:#fff;padding:6px 8px;text-align:left;font-size:8pt;font-weight:600}
tbody tr:nth-child(even){background:#f8f7f5}td{padding:5px 8px;border-bottom:1px solid #e8e6e4}td:first-child{font-style:italic;color:#334832}
.price{text-align:right}.stock{font-weight:600;font-size:8pt}.ins{color:#1e5a1e;background:#eaf2ea;border-radius:3px;padding:2px 6px}.oos{color:#b43c28;background:#fdecea;border-radius:3px;padding:2px 6px}
.footer{margin-top:16px;padding-top:10px;border-top:1px solid #e8e6e4;font-size:7.5pt;color:#999;display:flex;justify-content:space-between}
@media print{@page{size:A4 landscape;margin:12mm 10mm}thead th{background:#334832 !important;-webkit-print-color-adjust:exact;print-color-adjust:exact;color:#fff !important}tbody tr:nth-child(even){background:#f8f7f5 !important;-webkit-print-color-adjust:exact;print-color-adjust:exact}.ins{background:#eaf2ea !important;-webkit-print-color-adjust:exact;print-color-adjust:exact}.oos{background:#fdecea !important;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
</style></head><body>
<div class="header"><div><h1>Papervale Trees</h1><p>Spring / Summer 2026 Availability · $($sorted.Count) stock lines · papervaletrees.com</p></div><div class="meta">Generated $date<br>028 3085 0059 · info@papervaletrees.com</div></div>
<table><thead><tr><th>Botanical Name</th><th>Common Name</th><th>Pot Size</th><th>Height (cm)</th><th style="text-align:right">Price</th><th>Stock</th><th>SKU</th></tr></thead>
<tbody>$($tableRows -join '')</tbody></table>
<div class="footer"><span>Papervale Trees · 48 Old Newry Road, Rathfriland, Co. Down BT34 5BQ</span><span>Bareroot &amp; rootball: Nov–Mar only · Container-grown: year-round · Prices exc. delivery</span></div>
</body></html>
"@
    $htmlTmp = "$env:TEMP\availability-2026.html"
    $pdfOut  = "$outDir\availability-list-2026.pdf"
    $html | Set-Content $htmlTmp -Encoding UTF8

    $proc = Start-Process -FilePath $edge -Wait -PassThru -WindowStyle Hidden -ArgumentList @(
        '--headless', '--disable-gpu', '--no-pdf-header-footer',
        "--print-to-pdf=`"$pdfOut`"",
        "file:///$($htmlTmp.Replace('\','/'))"
    )
    if (Test-Path $pdfOut) {
        Write-Host "PDF generated: $pdfOut ($([math]::Round((Get-Item $pdfOut).Length/1KB,1)) KB)"
    } else {
        Write-Host "PDF generation failed (Edge exit: $($proc.ExitCode))"
    }
} else {
    Write-Host "Edge not found — skipping PDF (install Microsoft Edge to enable)"
}
