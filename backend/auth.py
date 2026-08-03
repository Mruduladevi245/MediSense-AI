from flask import Blueprint, request, jsonify
from database import mongo
import bcrypt

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.get_json(silent=True)

    if data is None:
        return jsonify({
            "message": "Invalid JSON"
        }), 400

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name or not email or not password:
        return jsonify({
            "message": "All fields are required"
        }), 400

    email = email.strip().lower()

    try:
        # Check if database is connected
        if mongo.db is None:
            return jsonify({
                "message": "Database connection not available"
            }), 500

        # Check existing user
        existing_user = mongo.db.users.find_one({
            "email": email
        })

        if existing_user:
            return jsonify({
                "message": "User already exists"
            }), 400

        # Hash password
        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        # Insert user
        mongo.db.users.insert_one({
            "name": name,
            "email": email,
            "password": hashed_password
        })

        return jsonify({
            "message": "Registration successful"
        }), 201

    except Exception as e:
        import traceback
        traceback.print_exc()

        return jsonify({
            "error": str(e)
        }), 500



@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json(silent=True)

    if data is None:
        return jsonify({
            "message": "Invalid JSON"
        }), 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "message": "Email and password are required"
        }), 400

    email = email.strip().lower()

    try:
        if mongo.db is None:
            return jsonify({
                "message": "Database connection not available"
            }), 500

        # Find user
        user = mongo.db.users.find_one({
            "email": email
        })

        if not user:
            return jsonify({
                "message": "User not found"
            }), 404


        # Check password
        if bcrypt.checkpw(
            password.encode("utf-8"),
            user["password"].encode("utf-8")
        ):

            return jsonify({
                "message": "Login successful",
                "user": {
                    "name": user["name"],
                    "email": user["email"]
                }
            }), 200


        return jsonify({
            "message": "Invalid password"
        }), 401


    except Exception as e:
        import traceback
        traceback.print_exc()

        return jsonify({
            "error": str(e)
        }), 500