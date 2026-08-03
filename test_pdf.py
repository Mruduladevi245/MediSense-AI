from pdf.report_pdf import ReportPDF
from pdf.doctor_summary_pdf import DoctorSummaryPDF
import os

os.makedirs("exports/pdf", exist_ok=True)

report = {
    "Hemoglobin": 13.5,
    "WBC": 6200,
    "Platelets": 250000,
    "Glucose": 95
}

ReportPDF.create(
    report,
    "exports/pdf/report.pdf"
)

DoctorSummaryPDF.create(
    "Patient is healthy. Continue a balanced diet and regular exercise.",
    "exports/pdf/doctor_summary.pdf"
)

print("PDFs Generated Successfully")