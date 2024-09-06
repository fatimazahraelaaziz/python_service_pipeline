from flask import Flask, request, jsonify
import os
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test-secret-key'  # Replace with a strong, random key
app.config['COUNTER_FILE'] = "/data/counter.txt"  # Set default path
csrf = CSRFProtect(app)

def read_counter():
    if os.path.exists(app.config['COUNTER_FILE']):
        with open(app.config['COUNTER_FILE'], "r") as f:
            return int(f.read().strip())
    else:
        return 0

def update_counter(counter):
    with open(app.config['COUNTER_FILE'], "w") as f:
        f.write(str(counter))

@app.route('/', methods=['GET'])
def get_count():
    counter = read_counter()
    return f"Current POST requests count: {counter}"

@app.route('/', methods=['POST'])
def increment_count():
    counter = read_counter()
    counter += 1
    update_counter(counter)
    return f"POST requests counter updated. Current count: {counter}"

@app.route('/health', methods=['GET'])
def health_check():
    try:
        read_counter()
        return jsonify({"status": "healthy"}), 200
    except Exception as e:
        return jsonify({"status": "unhealthy", "reason": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)