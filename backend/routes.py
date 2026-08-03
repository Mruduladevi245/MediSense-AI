import uuid

from flask import Blueprint, request, jsonify, send_file

from pdf_generator import generate_pdf
from voice_note import speak_text

routes = Blueprint("routes", __name__)


@routes.route("/")
def home():

    return {
        "project": "MediSense AI",
        "status": "Backend Running"
    }


@routes.route("/download_pdf", methods=["POST"])
def download_pdf():

    report = request.json

    # FIX: request.json is None if no JSON body (or wrong Content-Type)
    # was sent. Without this check, generate_pdf() would crash iterating
    # over None.items().
    if not report:
        return jsonify({
            "error": "No report data received"
        }), 400

    # FIX: generate_pdf always wrote to the same "Medical_Report.pdf" path,
    # so two requests at the same time could overwrite / corrupt each
    # other's download. Give each report a unique filename.
    filename = f"Medical_Report_{uuid.uuid4().hex[:8]}.pdf"
    pdf_path = generate_pdf(report, filename=filename)

    return send_file(
        pdf_path,
        as_attachment=True
    )


@routes.route("/voice", methods=["POST"])
def voice():

    data = request.json

    if not data:
        return jsonify({
            "error": "No data received"
        }), 400

    text = data.get("text")

    if not text:
        return jsonify({
            "error": "No text received"
        }), 400

    speak_text(text)

    return jsonify({
        "message": "Voice played successfully"
    })