from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph
)
from reportlab.lib.styles import getSampleStyleSheet
import os


class EmergencyPDF:

    @staticmethod
    def create(profile):

        os.makedirs("exports/pdf", exist_ok=True)

        filename = "exports/pdf/emergency_card.pdf"

        doc = SimpleDocTemplate(filename)

        styles = getSampleStyleSheet()

        story = []

        story.append(
            Paragraph(
                "<b>Emergency Medical Card</b>",
                styles["Title"]
            )
        )

        for key, value in profile.items():

            story.append(

                Paragraph(

                    f"<b>{key}</b>: {value}",

                    styles["BodyText"]

                )

            )

        doc.build(story)

        return filename