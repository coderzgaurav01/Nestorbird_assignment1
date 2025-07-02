# scraper.py
import requests
from bs4 import BeautifulSoup
import csv
from db import get_connection, create_table  


create_table()


url = "https://en.wikipedia.org/wiki/Web_scraping"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")


titles = []
title_level_list = [1, 2, 3, 4, 5]

for title_level in title_level_list:
    title_elements = soup.find_all(f"h{title_level}")
    for title_element in title_elements:
        tag = title_element.name
        text = title_element.text.strip()
        title = {"tag": tag, "title": text}
        titles.append(title)
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO wiki_headings (tag, title) VALUES (%s, %s)",
                (tag, text)
            )
            conn.commit()
        except Exception as e:
            print(f"[INSERT ERROR] Failed to insert: {text} – {e}")
        finally:
            conn.close()


with open("titles.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["tag", "title"])
    writer.writeheader()
    writer.writerows(titles)

print(" Scraping complete. Data saved to PostgreSQL and titles.csv.")
