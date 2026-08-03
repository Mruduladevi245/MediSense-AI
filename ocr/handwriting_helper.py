class HandwritingHelper:
    
    @staticmethod
    def improve(text):

        replacements = {

            "Paracetmol":"Paracetamol",

            "Amoxcillin":"Amoxicillin",

            "Ibuprofn":"Ibuprofen"

        }

        for wrong, correct in replacements.items():

            text = text.replace(
                wrong,
                correct
            )

        return text