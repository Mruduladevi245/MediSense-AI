class ProgressTracker:
    
    @staticmethod
    def progress(scores):

        if len(scores) < 2:

            return {

                "status": "Not enough reports.",

                "change": 0

            }

        change = scores[-1] - scores[0]

        if change > 0:

            status = "Health Improving"

        elif change < 0:

            status = "Health Declining"

        else:

            status = "No Significant Change"

        return {

            "status": status,

            "change": round(change, 2)

        }