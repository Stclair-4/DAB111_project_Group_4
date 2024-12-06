from flask import Flask, render_template, request
from utils.api_integration import get_data_from_api
import pandas as pd
import sqlite3

app = Flask(__name__, static_folder='static')

# SQLite database file
DATABASE = 'data.db'

# Group Members Information
GROUP_MEMBERS = [
    {"Name": "Chandresh A Sachala", "Id": "0874254"},
    {"Name": "Souravdeep Singh", "Id": "0862788"},
    {"Name": "Namrata C Chaudhari", "Id": "0872895"},
    {"Name": "Komalpreet Kaur", "Id": "0873963"}
]

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    # Pagination logic
    page = int(request.args.get('page', 1))  # Get the current page number, default is 1
    per_page = 10  # Number of rows per page
    conn = get_db_connection()
    
    # Fetch total row count
    total_rows = conn.execute('SELECT COUNT(*) FROM exerices').fetchone()[0]
    total_pages = (total_rows + per_page - 1) // per_page  # Calculate total pages
    
    # Fetch the required rows for the current page
    start = (page - 1) * per_page
    data = conn.execute('SELECT * FROM exerices LIMIT ? OFFSET ?', (per_page, start)).fetchall()
    conn.close()
    
    return render_template(
        'index.html', 
        title="Home",
        data=data, 
        page=page, 
        total_pages=total_pages
    )

@app.route('/exercises')
def show_exercise():
    endpoint = "/exercises?limit=10&offset=0"  # Update this to match your API's endpoint
    query_params = request.args.to_dict()  # Get optional query parameters
    api_response = get_data_from_api(endpoint, query_params)
    
    if api_response:
        return render_template('exercise.html', data=api_response)
    return render_template('exercise.html', title="Exercises", data=None, error="Failed to fetch data")

@app.route('/about')
def contact():
    return render_template('about.html', title="Contact", members=GROUP_MEMBERS)

if __name__ == '__main__':
    app.run(debug=True)
