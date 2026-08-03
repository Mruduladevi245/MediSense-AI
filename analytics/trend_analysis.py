class TrendAnalysis:
    
    @staticmethod
    def analyze(values):

        if len(values) < 2:

            return "Not enough data."

        if values[-1] > values[0]:

            return "Increasing Trend"

        elif values[-1] < values[0]:

            return "Decreasing Trend"

        return "Stable Trend"