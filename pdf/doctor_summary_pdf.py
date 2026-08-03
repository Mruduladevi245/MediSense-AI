from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


class DoctorSummaryPDF:

    @staticmethod
    def create(summary, filename):

        doc = SimpleDocTemplate(filename)

        styles = getSampleStyleSheet()

        story = [

            Paragraph(

                "Doctor Summary",

                styles["Title"]

            ),

            Paragraph(

                summary,

                styles["BodyText"]

            )

        ]

        doc.build(story)

        return filename