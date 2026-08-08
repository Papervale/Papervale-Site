#!/usr/bin/env python3
"""
update-reviews.py
Fetches latest customer reviews from Ecwid and updates data/ecwid-reviews.json

Setup (one-time):
  1. Copy .env.example to .env
  2. Fill in your Ecwid secret token in .env
  3. Keep .env in .gitignore (it's private)

Run from repo root:
  python3 scripts/update-reviews.py

Schedule this monthly to keep customer testimonials fresh
"""

import os
import sys
import json
import requests
from pathlib import Path
from datetime import datetime

# Load environment variables from .env file
def load_env():
    root = Path(__file__).parent.parent
    env_file = root / '.env'

    if env_file.exists():
        with open(env_file) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key.strip()] = value.strip()

# Load environment
load_env()

# Get configuration
ECWID_STORE_ID = os.environ.get('ECWID_STORE_ID', '73482057')
ECWID_TOKEN = os.environ.get('ECWID_SECRET_TOKEN', '')

if not ECWID_TOKEN or ECWID_TOKEN == 'your_secret_token_here':
    print("✗ Ecwid API token not configured\n")
    print("Setup:")
    print("  1. Copy .env.example to .env")
    print("  2. Edit .env and add your secret token:")
    print("     ECWID_SECRET_TOKEN=your_token_here\n")
    print("Get your secret token from:")
    print("  Ecwid Admin → Settings → API → Secret API token\n")
    print("⚠️  IMPORTANT: Never commit .env to git!")
    print("   It's in .gitignore to keep your token safe.")
    sys.exit(1)

# Fetch reviews
print("Fetching customer reviews from Ecwid...\n")

base_url = f'https://app.ecwid.com/api/v3/{ECWID_STORE_ID}'
headers = {'Authorization': f'Bearer {ECWID_TOKEN}'}

try:
    response = requests.get(
        f'{base_url}/products?limit=200',
        headers=headers,
        timeout=10
    )

    if response.status_code != 200:
        print(f"✗ API Error: {response.status_code}")
        print(f"Response: {response.text[:200]}")
        sys.exit(1)

    data = response.json()

    # Collect reviews
    all_reviews = []
    for product in data.get('items', []):
        if product.get('reviews'):
            for review in product['reviews']:
                all_reviews.append({
                    'product': product.get('name', 'Product'),
                    'productId': product.get('id'),
                    'rating': int(review.get('rating', 5)),
                    'text': review.get('text', ''),
                    'author': review.get('reviewer', {}).get('name') or review.get('author', 'Customer'),
                    'date': review.get('date', datetime.now().isoformat()),
                })

    if not all_reviews:
        print("⚠ No reviews found yet")
        print("Note: Reviews will appear once customers leave feedback in the shop\n")
        latest_reviews = []
    else:
        # Sort by date and get latest 4
        latest_reviews = sorted(
            all_reviews,
            key=lambda x: x.get('date', ''),
            reverse=True
        )[:4]

        print(f"✓ Found {len(all_reviews)} total reviews")
        print(f"✓ Showing latest {len(latest_reviews)} reviews\n")

        for review in latest_reviews:
            stars = '★' * review['rating'] + '☆' * (5 - review['rating'])
            print(f"  • {review['author']} ({stars})")
            print(f"    {review['text'][:70]}...")
            print(f"    Product: {review['product']}\n")

    # Save to JSON
    output_file = Path(__file__).parent.parent / 'data' / 'ecwid-reviews.json'
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, 'w') as f:
        json.dump(latest_reviews, f, indent=2)

    print(f"✓ Reviews saved: {output_file}")
    print("\n✓ Success! Reviews will display on your site.")

except requests.exceptions.RequestException as e:
    print(f"✗ Network error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"✗ Error: {e}")
    sys.exit(1)
