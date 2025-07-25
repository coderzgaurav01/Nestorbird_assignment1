# Wikipedia Web Scraping & PostgreSQL Storage

## 📌 Overview

This project is a Python-based web scraper that extracts headings (`<h1>` to `<h5>`) from the Wikipedia page on **Web Scraping** and stores them in both a **PostgreSQL database** and a **CSV file**. It demonstrates the use of Python libraries like `requests`, `BeautifulSoup`, `csv`, and `psycopg2` for data scraping, transformation, storage, and export.

---

## 📖 Assignment Brief

**Objective:**  
Scrape data from a dynamic website and store it in a PostgreSQL database. Then generate a CSV file with the same data.

### ✅ Assignment Steps

1. **Identifying a Dynamic Website:**
   - Disable JavaScript in your browser.
   - Load the target website (e.g., Wikipedia).
   - If the data does **not** appear, the site is dynamic (content loaded via JavaScript or API).
   - Wikipedia is partially dynamic, but for this task, the headings can be scraped statically using BeautifulSoup.

2. **Scraping Data:**
   - Use `requests` to fetch the HTML content.
   - Parse the data using `BeautifulSoup`.
   - Extract all `<h1>` to `<h5>` tags and store their content in a list of dictionaries.

3. **Storing Data in PostgreSQL:**
   - Create a PostgreSQL table named `wiki_headings` with fields: `tag` and `title`.
   - Insert all scraped headings into this table using `psycopg2`.

4. **Generating CSV File:**
   - Export the list of headings into a file called `titles.csv`.
   - Use the `csv` module with headers: `tag`, `title`.

---

## 🛠 Technologies Used

- Python 3.x
- `requests` - For sending HTTP requests.
- `BeautifulSoup4` - For parsing HTML content.
- `csv` - For generating CSV file.
- `psycopg2` - For PostgreSQL database connection.
- PostgreSQL - For storing the scraped data.

---

## 📁 File Structure


---

## 🔧 How to Run the Project

1. **Set Up PostgreSQL:**
   - Ensure PostgreSQL is installed and running.
   - Create a database (e.g., `project`).
   - In `db.py`, configure your connection settings.

2. **Install Required Python Libraries:**

   ```bash
   pip install requests beautifulsoup4 psycopg2

Run the Script:

bash

python assignment.py


Output:

Data will be inserted into the wiki_headings table.

A file titles.csv will be created in the working directory.

📝 Example Output (CSV)
tag	title
h1	Web scraping
h2	History
h3	Techniques
h4	Software
h5	Legal issues


