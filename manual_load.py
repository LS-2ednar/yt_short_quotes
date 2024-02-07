from sqlite3 import connect
import pandas as pd
from tqdm import tqdm

connection = connect("quotes.db")

# Read the Excel file into a DataFrame
df_excel = pd.read_excel("quotes.xlsx")

# Define the range of rows you want to iterate over
start_row = 0        # Starting row index
end_row   = 20000    # Ending row index (exclusive)

# Iterate over the specified range of rows
for index, row in tqdm(df_excel.iloc[start_row:end_row].iterrows()):
    quote_text  = row[0]
    author_text = row[1]  

    # Insert the quote and author into the database
    with connection:
        cursor = connection.cursor()
        cursor.execute('''INSERT INTO quotes (quote, author) VALUES (?, ?)''', (quote_text, author_text))

# Commit changes to the database
connection.commit()

# Close the database connection
connection.close()