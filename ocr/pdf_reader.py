import fitz


class PDFReader:

    @staticmethod
    def pdf_to_images(pdf_path):

        document = fitz.open(pdf_path)

        pages = []

        for page in document:

            pix = page.get_pixmap()

            image_path = f"temp_{page.number}.png"

            pix.save(image_path)

            pages.append(image_path)

        return pages