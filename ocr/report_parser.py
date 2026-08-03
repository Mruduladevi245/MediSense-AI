import re


class ReportParser:

    @staticmethod
    def parse(text):

        data = {}

        patterns = {

            "Hemoglobin":
            r"Hemoglobin[:\s]+([\d.]+)",

            "WBC":
            r"WBC[:\s]+([\d.]+)",

            "Platelets":
            r"Platelets[:\s]+([\d.]+)",

            "Glucose":
            r"Glucose[:\s]+([\d.]+)",

            "Cholesterol":
            r"Cholesterol[:\s]+([\d.]+)"

        }

        for key, pattern in patterns.items():

            match = re.search(
                pattern,
                text,
                re.IGNORECASE
            )

            if match:

                data[key] = match.group(1)

        return data