from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# SQLite Database connection function
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

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
    app.run(debug=True)
