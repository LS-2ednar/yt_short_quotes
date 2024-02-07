import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3

"""
This script extracts 8 quotes on a daily basis and adds them to the sqlite database
"""

# Connect to SQLite database (creates a new database if it doesn't exist)
conn = sqlite3.connect('quotes.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

"""
# Create a table to store quotes and authors
cursor.execute('''CREATE TABLE IF NOT EXISTS quotes (
                    id INTEGER PRIMARY KEY,
                    quote TEXT,
                    author TEXT
                )''')
"""
                
URLs = ["http://www.quotationspage.com/qotd.html","http://www.quotationspage.com/mqotd.html"]

for url in URLs:

    # Connect to the URL
    req = requests.get(url)

    # Stirrup the soup
    soup = BeautifulSoup(req.content,"html.parser")

    # Find all <dt> tags with class "quote"
    quote_elements = soup.find_all('dt', class_='quote')

    # Find all <dd> tags with class "author"
    author_elements = soup.find_all('dd', class_='author')

    # Loop through each quote and author pair
    for quote, author in zip(quote_elements, author_elements):
        # Extract the text from the <a> tag within <dt> for the quote
        quote_text = quote.find('a').text
        # Extract the text from the <b> tag within <dd> for the author
        author_text = author.find('b').text
        if "(" in author_text:
            author_text= author_text.split("(")[0]

        # Insert the quote and author into the database
        cursor.execute('''INSERT INTO quotes (quote, author) VALUES (?, ?)''', (quote_text, author_text))

    # Commit changes to the database
    conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()