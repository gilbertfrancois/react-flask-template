from flask import Flask
from flask import jsonify

app = Flask(__name__)

# ----------------------------------------------------------------------------------------------------------------------
# API
# ----------------------------------------------------------------------------------------------------------------------

@app.route('/api/version')
def home():
    return jsonify({"status": "success", "data": {"version": "1.0.0"}})


@app.route('/api/add/<a>/<b>', methods=['POST', 'GET'])
def add(a, b):
    try:
        c = float(a) + float(b)
        return jsonify({"status": "success", "data": {"answer": c}})
    except:
        return jsonify({"status": "error"})


# ----------------------------------------------------------------------------------------------------------------------
# MAIN
# ----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=42334, debug=True)
