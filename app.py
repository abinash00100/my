from flask import Flask, render_template, request, jsonify
import os
import json
import webbrowser
import threading

app = Flask(__name__)

# Ensure data directory exists
os.makedirs('data', exist_ok=True)


def open_browser():
    webbrowser.open('http://127.0.0.1:5000')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save_data():
    try:
        data = request.get_json()
        with open('data/tasks.json', 'w') as f:
            json.dump(data, f, indent=2)
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/load')
def load_data():
    try:
        if os.path.exists('data/tasks.json'):
            with open('data/tasks.json', 'r') as f:
                data = json.load(f)
            return jsonify(data)
        return jsonify({'descriptions': {}, 'members': {}})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    threading.Timer(1.25, open_browser).start()
    app.run(host="0.0.0.0", port=5000, debug=False)