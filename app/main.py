from flask import Flask, jsonify
from db import test_connection

app=Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Flask + PostgreSQL + PgBouncer + Docker is running!!"})

@app.route('/db-time')
def db_time():
    try:
        current_time = test_connection()
        return jsonify({"db_time": str(current_time)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

