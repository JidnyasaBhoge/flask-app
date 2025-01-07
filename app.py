from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    "host": "db",  # Docker service name for the database
    "user": "root",
    "password": "rootpassword",
    "database": "testdb"
}

@app.route('/')
def home():
    return "Welcome to the Two-Tier Flask Application!"

@app.route('/data')
def get_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("SELECT message FROM messages")
        result = cursor.fetchall()
        return jsonify(result)
    except mysql.connector.Error as err:
        return f"Error: {err}"
    finally:
        if connection:
            connection.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
