from .easyocr_engine import EasyOCREngine


class PrescriptionReader:

    @staticmethod
    def extract(image):

        text = EasyOCREngine.extract(image)

        return text