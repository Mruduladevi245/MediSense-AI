import re


class TextCleaner:

    @staticmethod
    def clean(text):

        text = re.sub(
            r"\s+",
            " ",
            text
        )

        text = text.replace("|", "I")

        text = text.replace("0O", "0")

        return text.strip()