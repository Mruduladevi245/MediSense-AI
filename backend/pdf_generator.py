from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os


def generate_pdf(report_data, filename="Medical_Report.pdf"):

    folder = "generated_reports"

    os.makedirs(folder, exist_ok=True)

    # FIX: accept a filename argument so callers (routes.py) can generate
    # a unique file per request instead of every request overwriting the
    # same Medical_Report.pdf.
    pdf_path = os.path.join(folder, filename)

    pdf = canvas.Canvas(pdf_path, pagesize=letter)

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(180, 770, "MediSense AI")

    pdf.setFont("Helvetica", 12)

    y = 730

    for key, value in report_data.items():

        pdf.drawString(
            60,
            y,
            f"{key}: {value}"
        )

        y -= 25

    pdf.save()

    return pdf_path