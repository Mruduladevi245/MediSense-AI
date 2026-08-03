import os


class ExportPDF:

    @staticmethod
    def create_folder():

        os.makedirs(

            "exports/pdf",

            exist_ok=True

        )

        return "exports/pdf"