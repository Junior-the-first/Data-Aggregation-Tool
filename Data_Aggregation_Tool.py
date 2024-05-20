import pandas as pd
import sqlite3
import json
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import requests

# Load Data from CSV
def load_csv(file_path):

    return pd.read_csv(file_path)

# Load Data from JSON
def load_json(file_path):
    
    with open(file_path) as f:
        data = json.load(f)
    return pd.DataFrame(data)

# Load Data from XML
def load_xml(file_path):
    
    tree = ET.parse(file_path)
    root = tree.getroot()
    data = [{elem.tag: elem.text for elem in child} for child in root]
    return pd.DataFrame(data)

# Scrape Data from HTML
def scrape_html(url):
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table')
    headers = [th.text for th in table.find('tr').find_all('th')]
    rows = []
    for tr in table.find_all('tr')[1:]:
        rows.append([td.text for td in tr.find_all('td')])
    return pd.DataFrame(rows, columns=headers)

# Create SQLite Database and Define Schema
def create_db(db_name):
    
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS data (
                    id INTEGER PRIMARY KEY,
                    source TEXT,
                    data TEXT
                )''')
    conn.commit()
    conn.close()

# Insert Data into SQLite Database
def insert_data(db_name, source, data):
    
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    for record in data.to_dict(orient='records'):
        c.execute("INSERT INTO data (source, data) VALUES (?, ?)", (source, json.dumps(record)))
    conn.commit()
    conn.close()

# Parameterized Queries
def query_data(db_name, query):
    
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute(query)
    results = c.fetchall()
    conn.close()
    return results

# Main function
def main():
    db_name = 'aggregated_data.db'
    
    # Create Database
    create_db(db_name)
    print("Database Created Successfully")
    
    # Load data from various sources
    csv_data = load_csv('input_data.csv')
    json_data = load_json('input_data.json')
    xml_data = load_xml('input_data.xml')
    html_data = scrape_html('http://example.com/data.html')
    
    # Insert data into the database
    insert_data(db_name, 'CSV', csv_data)
    insert_data(db_name, 'JSON', json_data)
    insert_data(db_name, 'XML', xml_data)
    insert_data(db_name, 'HTML', html_data)
    print("Data Inserted Successfully")
    
    # Example parameterized query
    query = "SELECT * FROM data WHERE source = 'CSV'"
    results = query_data(db_name, query)
    print("Query Results:", results)

# Run the main function
if __name__ == "__main__":
    main()