# Customer Reviews & Testimonials

Auto-updating customer testimonials from Ecwid displayed on the homepage.

---

## Setup (One-Time)

### 1. Create `.env` file with your API credentials

```bash
# From repo root, create .env from the template:
cp .env.example .env
```

### 2. Add your Ecwid Secret Token

Edit `.env` and replace `your_secret_token_here`:

```env
ECWID_STORE_ID=73482057
ECWID_SECRET_TOKEN=your_secret_token_here
```

**Get your token:**
- Log in to https://my.ecwid.com
- Settings → API → Copy **Secret API token**
- Paste into `.env`

### 3. Verify `.env` is in `.gitignore`

✓ Already configured — your `.env` will never be committed to git

---

## Usage

### Python (Recommended for Mac/Linux)

```bash
python3 scripts/update-reviews.py
```

### PowerShell (Windows)

```powershell
pwsh scripts/update-reviews.ps1
```

Both scripts:
- Load credentials from `.env`
- Fetch latest reviews from Ecwid
- Save top 4 reviews to `data/ecwid-reviews.json`
- Update homepage automatically

---

## Automation

### Option 1: macOS/Linux Cron

Add to crontab to run monthly (e.g., 1st of each month at 2 AM):

```bash
crontab -e

# Add this line:
0 2 1 * * cd /path/to/papervale-site && python3 scripts/update-reviews.py >> logs/reviews-update.log 2>&1
```

### Option 2: Windows Task Scheduler

1. Open Task Scheduler
2. Create Basic Task
3. Name: "Update Papervale Reviews"
4. Trigger: Monthly (1st of month at 2 AM)
5. Action: Start Program
   - Program: `pwsh`
   - Arguments: `scripts/update-reviews.ps1`
   - Start in: `C:\path\to\papervale-site`

### Option 3: GitHub Actions (Recommended)

Add `.github/workflows/update-reviews.yml`:

```yaml
name: Update Reviews

on:
  schedule:
    - cron: '0 2 1 * *'  # 1st of each month at 2 AM UTC

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
      - name: Update reviews
        env:
          ECWID_SECRET_TOKEN: ${{ secrets.ECWID_TOKEN }}
        run: python3 scripts/update-reviews.py
      - name: Commit changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add data/ecwid-reviews.json
          git commit -m "chore: update customer reviews" || echo "No changes"
          git push
```

Then add your secret token to GitHub:
- Go to Settings → Secrets and variables → Actions
- New repository secret: `ECWID_TOKEN`
- Paste your secret token

---

## How It Works

1. **Script fetches reviews** from Ecwid API using your secret token
2. **Selects top 4 latest** reviews
3. **Saves to `data/ecwid-reviews.json`**
4. **Homepage JavaScript** automatically loads and displays them
5. **Updates monthly** (or whenever you run the script)

---

## Viewing Reviews

Reviews automatically display on:
- Homepage below "From small back gardens to large commercial projects..."
- In a carousel with ratings, customer names, and products
- Responsive 4-card grid that works on mobile

---

## Security

⚠️ **Important:**

- `.env` is in `.gitignore` — never committed
- Your API token stays local/private
- Only the generated `data/ecwid-reviews.json` is public (contains review text, not credentials)
- Rotate your token annually for security

---

## Troubleshooting

### "API token not configured"
- Check `.env` exists in repo root
- Verify `ECWID_SECRET_TOKEN` is set (not `your_secret_token_here`)

### "403 Forbidden"
- Token may be expired
- Check in Ecwid: Settings → API → regenerate if needed
- Update `.env` with new token

### "No reviews found"
- Customers haven't left reviews yet in the shop
- Check Ecwid dashboard for reviews
- Script will auto-populate once reviews exist

### Script runs but nothing updates
- Check `data/ecwid-reviews.json` was created
- Review HTML on homepage — should show reviews if they exist
- Check browser console for JavaScript errors

---

## Manual Testing

```bash
# Test the script locally
python3 scripts/update-reviews.py

# Check output
cat data/ecwid-reviews.json
```

---

## Files

- `.env` — Your API credentials (private, gitignored)
- `.env.example` — Template (commit this)
- `scripts/update-reviews.py` — Fetch script (Python)
- `scripts/update-reviews.ps1` — Fetch script (PowerShell)
- `data/ecwid-reviews.json` — Generated reviews (public)
- `index.html` — Homepage with carousel component
