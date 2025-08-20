from flask import Flask, jsonify, request
from flasgger import Swagger
from db import test_connection, create_user, get_users, get_user_by_id, update_user, delete_user

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/')
def home():
    """Health check endpoint
    ---
    responses:
      200:
        description: API is running
    """
    return jsonify({"message": "Flask + PostgreSQL + PgBouncer + Docker is running!!"})

@app.route('/db-time')
def db_time():
    """Get current database time
    ---
    responses:
      200:
        description: Current DB time
        schema:
          type: object
          properties:
            db_time:
              type: string
    """
    try:
        current_time = test_connection()
        return jsonify({"db_time": str(current_time)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------- User CRUD APIs ----------

@app.route('/users', methods=['POST'])
def add_user():
    """Create a new user
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - name
            - email
          properties:
            name:
              type: string
            email:
              type: string
    responses:
      201:
        description: User created successfully
    """
    data = request.get_json()
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Name and email required"}), 400
    user = create_user(data["name"], data["email"])
    return jsonify({"message": "User created", "user": user}), 201

@app.route('/users', methods=['GET'])
def list_users():
    """List all users
    ---
    responses:
      200:
        description: A list of users
    """
    users = get_users()
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get user by ID
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: User found
      404:
        description: User not found
    """
    user = get_user_by_id(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

@app.route('/users/<int:user_id>', methods=['PUT'])
def modify_user(user_id):
    """Update user (full)
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            email:
              type: string
    responses:
      200:
        description: User updated successfully
      404:
        description: User not found
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    user = update_user(user_id, data.get("name"), data.get("email"))
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "User updated", "user": user})

@app.route('/users/<int:user_id>', methods=['PATCH'])
def patch_user(user_id):
    """Partially update user
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            email:
              type: string
    responses:
      200:
        description: User partially updated successfully
      404:
        description: User not found
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    user = update_user(user_id, data.get("name"), data.get("email"))
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "User partially updated", "user": user})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def remove_user(user_id):
    """Delete user
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: User deleted successfully
      404:
        description: User not found
    """
    deleted = delete_user(user_id)
    if not deleted:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "User deleted"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
