import json


class JSONFormatter:

    @staticmethod
    def format(data):

        return json.dumps(
            data,
            indent=4
        )