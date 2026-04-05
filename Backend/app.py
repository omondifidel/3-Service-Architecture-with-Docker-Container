from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # This allows the frontend to talk to the backend

@app.route('/api/balance', methods=['GET'])
def get_balance():
    # In a real bank, this would come from a Database
    return jsonify({
        "status": "success",
        "balance": 250750.45,
        "currency": "USD"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)