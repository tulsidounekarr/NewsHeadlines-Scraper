from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from datetime import datetime

app = Flask(__name__)

def get_headlines():
    url = "https://www.bbc.com/news"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    tags = soup.find_all(["h3", "h2", "a"], string=True)

    headlines = []
    for tag in tags:
        text = tag.get_text(strip=True)
        if 30 <= len(text) <= 120 and not text.startswith("BBC"):
            headlines.append(text)

    return list(dict.fromkeys(headlines))[:10]

@app.route("/")
def index():
    headlines = get_headlines()
    today = datetime.now().strftime("%d %B %Y")
    return render_template("index.html", headlines=headlines, date=today)

if __name__ == "__main__":
    app.run(debug=True)
