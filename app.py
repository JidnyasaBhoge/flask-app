from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    """
    A simple route that returns a 'Hello, World!' message.
    """
    return jsonify(message="Hello, World!")

@app.route('/status')
def status():
    """
    A simple status endpoint to check if the app is running.
    """
    return jsonify(status="Running")

if __name__ == '__main__':
    # Run the app on port 5000 and make it accessible externally
    app.run(host='0.0.0.0', port=5000)
