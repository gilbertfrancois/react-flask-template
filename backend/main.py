from flask import Flask
from flask import jsonify
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/status')
def home():
    return jsonify({"success": True, "data": {"status": "ok"}})


if __name__ == '__main__':
    app.run(port=5000, debug=True)
