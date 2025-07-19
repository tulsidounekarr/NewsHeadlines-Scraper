import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv

# Step 1: URL and headers
url = "https://www.bbc.com/news"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115 Safari/537.36"
}

# Step 2: Make request
response = requests.get(url, headers=headers)

# Step 3: Check and parse HTML
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Step 4: Find all possible headline tags (based on structure in July 2025)
    headline_tags = soup.find_all(["h3", "h2", "a"], string=True)

    # Step 5: Filter and clean meaningful headlines
    headlines = []
    for tag in headline_tags:
        text = tag.get_text(strip=True)
        if (30 <= len(text) <= 120) and not text.startswith("BBC"):
            headlines.append(text)

    # Remove duplicates and limit
    unique_headlines = list(dict.fromkeys(headlines))[:10]

    # Step 6: Save to CSV
    today = datetime.now().strftime("%Y-%m-%d")
    with open("headlines.csv", "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["No.", "Headline", "Date"])
        for i, headline in enumerate(unique_headlines, start=1):
            writer.writerow([i, headline, today])

    # Step 7: Print output
    print("\n📰 Top 10 BBC News Headlines:\n")
    for i, headline in enumerate(unique_headlines, start=1):
        print(f"{i}. {headline}")

else:
    print(f"❌ Request failed with status code {response.status_code}")
