from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet


class ReportPDF:

    @staticmethod
    def create(report, filename):

        doc = SimpleDocTemplate(filename)

        styles = getSampleStyleSheet()

        elements = []

        elements.append(
            Paragraph(
                "Medical Report Analysis",
                styles["Title"]
            )
        )

        elements.append(Spacer(1, 20))

        table_data = [

            ["Parameter", "Value"]

        ]

        for key, value in report.items():

            table_data.append([key, str(value)])

        table = Table(table_data)

        table.setStyle(TableStyle([

            ("BACKGROUND", (0,0), (-1,0), colors.darkblue),

            ("TEXTCOLOR", (0,0), (-1,0), colors.white),

            ("GRID", (0,0), (-1,-1), 1, colors.black),

            ("BACKGROUND", (0,1), (-1,-1), colors.beige),

            ("BOTTOMPADDING", (0,0), (-1,0), 10)

        ]))

        elements.append(table)

        doc.build(elements)

        return filename