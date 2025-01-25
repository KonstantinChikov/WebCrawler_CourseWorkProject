import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser
import logging
# import json
# import sqlite3

logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

def is_allowed_to_scrape(url):
    """
    Checks if scraping the given URL is allowed based on the site's robots.txt file.
    
    Args:
        url (str): The URL to check.
        
    Returns:
        bool: True if scraping is allowed, False otherwise.
    """
    parsed_url = urlparse(url)
    robots_url = f"{parsed_url.scheme}://{parsed_url.netloc}/robots.txt"
    rp = RobotFileParser()
    rp.set_url(robots_url)
    try:
        rp.read()
        for entry in rp.entries:
            print(entry)
        return rp.can_fetch("*", url)
    except:
        print(f"Couldn't retrieve or parse robots.txt for {robots_url}. Proceeding with caution.")
        return False  # Default to False if there's an issue with robots.txt

def fetch_content(url, selector):
    """
    Fetches and parses content from the provided URL based on the HTML selector, if allowed by robots.txt.
    
    Args:
        url (str): The URL of the site to parse.
        selector (dict): Dictionary with tag and attributes to find the desired HTML elements.
                         Example: {'tag': 'h1', 'class_': 'entry-title'}
    
    Returns:
        list: A list of text content from the matched elements.
    """
    if not is_allowed_to_scrape(url):
        print(f"Scraping disallowed by robots.txt for {url}. Skipping...")
        return []

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for non-2xx responses
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    elements = soup.find_all(selector['tag'], class_=selector.get('class_'))
    return [element.get_text() for element in elements]

def parse_multiple_sites(sites):
    """
    Parses multiple sites and extracts content based on their individual selectors.
    
    Args:
        sites (list of dict): List of dictionaries where each dictionary contains 'url' and 'selector'.
    
    Returns:
        dict: A dictionary with URLs as keys and extracted content as values.
    """
    results = {}
    for site in sites:
        url = site['url']
        selector = site['selector']
        print(f"Checking permission and parsing content from {url}...")
        results[url] = fetch_content(url, selector)
    
    return results

# Example usage
sites = [
    {'url': 'https://dnes.bg', 'selector': {'tag': 'h1', 'class_': ''}},
    {'url': 'https://amazon.com', 'selector': {'tag': 'h2', 'class_': ''}},
    {'url': 'https://scrapethissite.com/pages', 'selector': {'tag': 'h3', 'class_': 'page-title'}},
    # Add more sites and selectors as needed
]

parsed_data = parse_multiple_sites(sites)

# CSV
# import csv
# with open('posts.csv', 'w', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=['url', 'content'])
#     writer.writeheader()

#     for url, data in parsed_data.items():
#         print(f"Content from {url}:")
#         for item in data:
#             t = {
#                 'url': url,
#                 'content': item
#                 }
#             writer.writerow(t)
#             print(" - ", item)
#         print("Done")

# import json, data is already in json format (look in the repo), json.dump(...)

# SQLITE
# use_storage = False

# if use_storage:
#     # Connect to SQLite database (or create one)
#     conn = sqlite3.connect('scraped_data.db')

#     # Create a cursor object to execute SQL commands
#     cursor = conn.cursor()

#     # Create a table for storing scraped data
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS posts (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         url TEXT,
#         content TEXT
#     )
#     ''')

#     # Insert data into the table
#     tuples = []
#     for url, data in parsed_data.items():
#         for item in data:
#             t = (url, item)
#             tuples.append(t)

#     cursor.executemany('INSERT INTO posts (url, content) VALUES (?, ?)', 
#                     tuples)

#     # Commit the transaction and close the connection
#     conn.commit()
#     conn.close()

# conn = sqlite3.connect('scraped_data.db')
# rows = conn.execute('SELECT * FROM posts')
# for row in rows:
#     print(f'Id: {row[0]}')
#     print(f'Url: {row[1]}')
#     print(f'Content: {row[2]}')
#     print()

# conn.close()

import psycopg2 # type: ignore

# PostgreSQL
use_storage = False

if use_storage:
    # Connect to SQLite database (or create one)
    conn = psycopg2.connect(database="test_db", user="admin", password="root", host="postgres_db", port=5432)

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Create a table for storing scraped data
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
        url TEXT,
        content TEXT
    )
    ''')

    # Insert data into the table
    tuples = []
    for url, data in parsed_data.items():
        for item in data:
            t = (url, item)
            tuples.append(t)

    cursor.executemany('INSERT INTO posts (url, content) VALUES (%s, %s)', 
                    tuples)

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

conn = psycopg2.connect(database="test_db", user="admin", password="root", host="postgres_db", port=5432)
cursor = conn.cursor()
rows = cursor.execute('SELECT * FROM posts')
for row in cursor:
    print(row)

conn.close()