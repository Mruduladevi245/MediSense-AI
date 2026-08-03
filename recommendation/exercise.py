class Exercise:
    
    @staticmethod
    def recommend(age):

        if age < 18:

            return [
                "Cycling",
                "Running",
                "Outdoor Games"
            ]

        elif age < 40:

            return [
                "Gym",
                "Jogging",
                "Yoga"
            ]

        return [
            "Walking",
            "Light Yoga",
            "Stretching"
        ]