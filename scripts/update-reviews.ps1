# update-reviews.ps1
# Fetches latest customer reviews from Ecwid and updates data/ecwid-reviews.json
#
# Setup (one-time):
#   1. Copy .env.example to .env
#   2. Fill in your Ecwid secret token in .env
#   3. Keep .env in .gitignore (it's private)
#
# Run from repo root:
#   pwsh scripts/update-reviews.ps1
#
# Schedule this monthly to keep customer testimonials fresh

$root    = $PSScriptRoot | Split-Path -Parent
$envFile = "$root\.env"
$outDir  = "$root\data"
$storeId = '73482057'

if (-not (Test-Path $outDir)) { New-Item -ItemType Directory -Path $outDir -Force | Out-Null }

# ── Load environment variables from .env file ──────────────────────────────────
if (Test-Path $envFile) {
    Get-Content $envFile | Where-Object { $_ -match '^\w' } | ForEach-Object {
        $key, $value = $_ -split '=', 2
        [System.Environment]::SetEnvironmentVariable($key.Trim(), $value.Trim())
    }
}

# Get API token from environment
$EcwidToken = $env:ECWID_SECRET_TOKEN

if (-not $EcwidToken -or $EcwidToken -eq 'your_secret_token_here') {
    Write-Host "✗ Ecwid API token not configured"
    Write-Host ""
    Write-Host "Setup:"
    Write-Host "  1. Copy .env.example to .env"
    Write-Host "  2. Edit .env and add your secret token:"
    Write-Host "     ECWID_SECRET_TOKEN=your_token_here"
    Write-Host ""
    Write-Host "Get your secret token from:"
    Write-Host "  Ecwid Admin → Settings → API → Secret API token"
    Write-Host ""
    Write-Host "⚠️  IMPORTANT: Never commit .env to git!"
    Write-Host "    It's in .gitignore to keep your token safe."
    exit 1
}

Write-Host "Fetching customer reviews from Ecwid..."

$uri = "https://app.ecwid.com/api/v3/$storeId/products?limit=200"
$headers = @{ Authorization = "Bearer $EcwidToken" }

try {
    $response = Invoke-RestMethod -Uri $uri -Headers $headers

    $allReviews = [System.Collections.Generic.List[PSCustomObject]]::new()

    foreach ($product in $response.items) {
        if ($product.reviews) {
            foreach ($review in $product.reviews) {
                $allReviews.Add([PSCustomObject]@{
                    product    = $product.name
                    productId  = $product.id
                    rating     = [int]($review.rating ?? 5)
                    text       = $review.text
                    author     = $review.reviewer.name ?? $review.author ?? 'Customer'
                    date       = $review.date ?? (Get-Date -Format 'o')
                })
            }
        }
    }

    if ($allReviews.Count -eq 0) {
        Write-Host "⚠ No reviews found yet"
        Write-Host "Note: Reviews will appear once customers leave feedback in the shop"
        $outFile = "$outDir\ecwid-reviews.json"
        @() | ConvertTo-Json | Set-Content $outFile -Encoding UTF8
        Write-Host "Created empty reviews file: $outFile"
    } else {
        # Sort by date descending and take latest 4
        $latestReviews = $allReviews | Sort-Object -Property date -Descending | Select-Object -First 4

        Write-Host "✓ Found $($allReviews.Count) total reviews"
        Write-Host "✓ Showing latest $($latestReviews.Count) reviews"

        foreach ($review in $latestReviews) {
            Write-Host "  • $($review.author) ($($review.rating)★) - $($review.product)"
        }

        # Convert to JSON and save
        $json = $latestReviews | ConvertTo-Json -Depth 10
        $outFile = "$outDir\ecwid-reviews.json"
        $json | Set-Content $outFile -Encoding UTF8

        Write-Host ""
        Write-Host "✓ Reviews updated: $outFile"
    }

} catch {
    Write-Host "✗ Error fetching reviews: $_"
    exit 1
}

Write-Host ""
Write-Host "To schedule monthly updates on Windows:"
Write-Host "  Use Task Scheduler to run this script monthly"
Write-Host ""
Write-Host "Or add to your CI/CD pipeline to run on schedule"
