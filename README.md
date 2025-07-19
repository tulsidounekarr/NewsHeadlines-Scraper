# NewsHeadlines-Scraper
To develop a Python script that automatically scrapes the latest top headlines from a popular news website and stores them in a .txt file for offline reading or analysis. 


🕸️📝 News Headlines Web Scraper

🚀 Features: 

-🌐 Scrapes the latest top news headlines from BBC
-📄 Saves the results to a CSV file (headlines.csv)
-🔁 Removes duplicate headlines automatically
-📅 Adds current date to each headline entry
-🧠 Filters only meaningful and readable headlines (30–120 characters)

---

🛠️ Tools & Technologies:

🐍 Python 3.x
🔗 requests — To fetch webpage content
🍲 BeautifulSoup — For HTML parsing
📦 csv, datetime — For data handling and formatting

---

💡 Project Objective:

Automate the extraction of news headlines from a trusted source to reduce manual browsing, useful for research, content ideas, or news aggregation.

---

📦 Requirements:
Python 3.x

---

Install dependencies:

-bash
-Copy code
-pip install requests beautifulsoup4

---

▶ How to Run
-bash
-Copy code
-python scraper.py

This will:
-Scrape the top 10 BBC News headline
-Save them into headlines.csv
-Display them in the terminal

---

📂 Project Structure
bash
Copy code
scraper.py        # Main Python script
headlines.csv     # Output file with news headlines
README.md         # Project documentation

---
📝 Sample Output (Terminal)
bash
Copy code
📰 Top 10 BBC News Headlines:

1. AI tools to be regulated by new UK tech bill
2. Ukraine peace talks continue despite setbacks
3. Scientists discover new coral reef in Maldives
...

---

🎯 Hints & Mini Guide:

1. Use requests.get() to fetch HTML
2. Use BeautifulSoup to parse <h2>, <h3>, or <a> tags
3. Use .get_text() and filtering for headline quality
4. Save results using the csv module

---

🔑 Key Concepts:

1. HTTP Requests
2. Web Scraping
3. HTML Parsing
4. File Handling (CSV)

 ---

👩‍💻 Author
GitHub: @tulsidounekarr

 ---

📄 License
This project is open-source and available under the MIT License.
