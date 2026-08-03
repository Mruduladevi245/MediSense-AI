class Calories:
    
    @staticmethod
    def daily(age, gender, weight, height):

        if gender.lower() == "male":

            return int(
                10 * weight +
                6.25 * height -
                5 * age + 5
            )

        return int(
            10 * weight +
            6.25 * height -
            5 * age - 161
        )