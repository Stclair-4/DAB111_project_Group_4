import sqlite3
import pandas as pd

DATABASE = 'data.db'
CSV_FILE = 'gym_members_exercise_tracking.csv'

# Create SQLite database and table
conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

# Load data from CSV file into SQLite database
df = pd.read_csv(CSV_FILE)
df.to_sql('exerices', conn, if_exists='replace', index=False)

conn.commit()
conn.close()
