"""
Level 3 - Task 1: Build a Web Scraper
Extracts data from a website using the requests + BeautifulSoup libraries.

We scrape https://quotes.toscrape.com - a site built specifically for
practicing web scraping. It's safe and legal to scrape for learning.

Install requirements first:
    pip install requests beautifulsoup4
"""

import requests
from bs4 import BeautifulSoup

def scrape_quotes(url="https://quotes.toscrape.com"):
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch page. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    quotes_data = []
    # Every quote on the page is inside a <div class="quote">
    for quote_block in soup.find_all("div", class_="quote"):
        text = quote_block.find("span", class_="text").get_text(strip=True)
        author = quote_block.find("small", class_="author").get_text(strip=True)
        tags = [tag.get_text(strip=True) for tag in quote_block.find_all("a", class_="tag")]

        quotes_data.append({
            "text": text,
            "author": author,
            "tags": tags
        })

    return quotes_data


if __name__ == "__main__":
    quotes = scrape_quotes()

    print(f"Scraped {len(quotes)} quotes:\n")
    for i, quote in enumerate(quotes, start=1):
        print(f"{i}. \"{quote['text']}\" - {quote['author']}")
        print(f"   Tags: {', '.join(quote['tags'])}\n")
