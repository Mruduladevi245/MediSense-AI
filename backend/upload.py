import os

from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename

import config

upload_bp = Blueprint("upload", __name__)

# FIX: use the same UPLOAD_FOLDER as the rest of the app (from config/.env)
# instead of a separate hardcoded constant that could silently diverge.
UPLOAD_FOLDER = config.UPLOAD_FOLDER


@upload_bp.route("/upload", methods=["POST"])
def upload():

    # FIX: request.files["file"] raises a raw KeyError (500 error) if the
    # client doesn't send a file. Check for it and return a clean 400.
    if "file" not in request.files:
        return jsonify({
            "message": "No file part in request"
        }), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({
            "message": "No file selected"
        }), 400

    # FIX: sanitize the filename to prevent path traversal
    # (e.g. "../../etc/passwd" or absolute paths).
    filename = secure_filename(file.filename)

    if not filename:
        return jsonify({
            "message": "Invalid filename"
        }), 400

    # FIX: ensure the upload folder actually exists before saving into it,
    # otherwise file.save() raises FileNotFoundError.
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(path)

    return jsonify({
        "message": "Uploaded Successfully",
        "path": path
    })