from flask import Flask
from flask_cors import CORS

import config
from database import mongo

from auth import auth_bp
from upload import upload_bp
from routes import routes


app = Flask(__name__)

# Configuration
app.config["MONGO_URI"] = config.MONGO_URI
app.config["SECRET_KEY"] = config.SECRET_KEY
app.config["UPLOAD_FOLDER"] = config.UPLOAD_FOLDER


# Initialize MongoDB
mongo.init_app(app)


# Check MongoDB connection
with app.app_context():
    try:
        if mongo.db is None:
            raise Exception("MongoDB database not initialized")

        mongo.db.command("ping")
        print("MongoDB connection: OK")

    except Exception as e:
        print("MongoDB connection failed:", e)


# Enable CORS
CORS(app)


# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(upload_bp)
app.register_blueprint(routes)


# Run Flask server
if __name__ == "__main__":
    app.run(
        debug=True,
        use_reloader=False,
        host="127.0.0.1",
        port=5000
    )