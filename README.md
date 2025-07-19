# 📰 News Headlines Scraper

A Python script that scrapes the top 10 latest headlines from the BBC News website and saves them to a CSV file.

## 📌 Objective

Automate data collection of real-time news headlines from a public website using Python.

---

## 🛠 Tools & Libraries

- Python 3
- `requests`
- `BeautifulSoup` (from `bs4`)
- `csv`, `datetime` modules

---

## 🚀 How It Works

1. Sends an HTTP GET request to [BBC News](https://www.bbc.com/news)
2. Parses the HTML using BeautifulSoup
3. Extracts top 10 readable headlines
4. Saves them to a file: `headlines.csv`
5. Also prints the headlines to the terminal

---

## 📁 Output Example

📄 Output File
headlines.csv — contains columns:

Serial number

Headline text

Scrape date

🔑 Key Concepts
Web scraping

HTTP requests

HTML parsing

Data automation

✅ Author
Made by [Your Name] for internship project submission.

yaml
Copy code

