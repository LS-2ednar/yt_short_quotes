from sqlite3 import connect
import pandas as pd

# Connect to database
connection = connect("quotes.db")

# Load data from the database into a DataFrame
df = pd.read_sql('SELECT quote, author FROM quotes', connection)

# Find duplicates in the DataFrame
duplicates = df[df.duplicated()]

if not duplicates.empty:
    print("Duplicates found:")
    print(duplicates)
    
    # Remove duplicates from the database
    with connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM quotes WHERE ROWID NOT IN (SELECT MIN(ROWID) FROM quotes GROUP BY quote, author)')
        print("Duplicates removed.")

else:
    print("No duplicates found.")

# Close the database connection
connection.close()