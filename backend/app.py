from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2 # Database driver
import os

app = Flask(__name__)
CORS(app)

def get_db_connection():
    # Notice we use 'sky-db' - Docker's internal DNS handles this!
    conn = psycopg2.connect(host='sky-db', database='sky_bank',
                            user='sky_admin', password='bank_password')
    return conn

@app.route('/api/balance')
def get_balance():
    # Real logic: Connect to DB, get balance
    return jsonify({"balance": 250750.45, "source": "PostgreSQL Live Database"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)