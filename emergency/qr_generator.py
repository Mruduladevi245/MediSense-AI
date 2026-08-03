import json
import qrcode
import os


class QRGenerator:

    @staticmethod
    def generate(profile, filename):

        os.makedirs("exports/qr", exist_ok=True)

        filepath = os.path.join(
            "exports/qr",
            filename
        )

        qr = qrcode.QRCode(

            version=1,

            box_size=10,

            border=5

        )

        qr.add_data(

            json.dumps(profile)

        )

        qr.make(fit=True)

        image = qr.make_image(

            fill_color="black",

            back_color="white"

        )

        image.save(filepath)

        return filepath