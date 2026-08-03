from .easyocr_engine import EasyOCREngine


class MedicineScanner:

    @staticmethod
    def scan(image):

        text = EasyOCREngine.extract(image)

        medicines = []

        for line in text.split("\n"):

            if len(line) > 3:

                medicines.append(line)

        return medicines