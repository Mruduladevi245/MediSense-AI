from statistics import mean


class Statistics:

    @staticmethod
    def average(values):

        if not values:
            return 0

        return round(mean(values), 2)

    @staticmethod
    def minimum(values):

        if not values:
            return 0

        return min(values)

    @staticmethod
    def maximum(values):

        if not values:
            return 0

        return max(values)

    @staticmethod
    def summary(values):

        return {

            "Average": Statistics.average(values),

            "Minimum": Statistics.minimum(values),

            "Maximum": Statistics.maximum(values)
        }