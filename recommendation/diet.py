class DietPlanner:
    
    @staticmethod
    def recommend(score):

        if score >= 90:

            return [
                "Balanced Diet",
                "Fresh Fruits",
                "Vegetables",
                "Milk",
                "Whole Grains"
            ]

        elif score >= 70:

            return [
                "Low Sugar Diet",
                "Protein Rich Food",
                "Nuts",
                "Green Vegetables"
            ]

        else:

            return [
                "Consult Dietician",
                "Reduce Junk Food",
                "Increase Water Intake",
                "Healthy Meals"
            ]