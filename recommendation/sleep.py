class SleepPlanner:
    
    @staticmethod
    def recommend(age):

        if age < 18:
            return "8–10 hours"

        if age < 65:
            return "7–9 hours"

        return "7–8 hours"