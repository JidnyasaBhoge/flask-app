
from flask import Flask, jsonify
import sqlite3
import os

app = Flask(__name__)

# SQLite Database connection function
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Initialize the database if not exists
def init_db():
    if not os.path.exists('database.db'):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        # Create a 'users' table
        c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        ''')

        # Insert some example data
        c.execute('INSERT INTO users (name) VALUES ("Alice")')
        c.execute('INSERT INTO users (name) VALUES ("Bob")')

        conn.commit()
        conn.close()

# Home route
@app.route('/')
def home():
    return "Welcome to the Two-Tier Flask App!"

# Fetch data from the database route
@app.route('/data')
def get_data():
    conn = get_db_connection()
    data = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    
    return jsonify([dict(row) for row in data])

if __name__ == '__main__':
    init_db()  # Call the function to initialize the database
    app.run(debug=True)
