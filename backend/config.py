import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise RuntimeError(
        "MONGO_URI is not set. Add it to your .env file, e.g.\n"
        "MONGO_URI=mongodb+srv://mruduladevi026:MediSense15@<cluster>/<db>"
    )

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "medisense_secret_key"
)

UPLOAD_FOLDER = os.getenv(
    "UPLOAD_FOLDER",
    "uploads"
)

# FIX: removed `print("DEBUG MONGO URI:", MONGO_URI)`. That line printed
# your full Mongo connection string — including the username and
# password — to the console/logs on every startup. Never log secrets,
# even in development.