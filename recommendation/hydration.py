class Hydration:
    
    @staticmethod
    def recommend(weight):

        liters = round(weight * 0.035, 1)

        return f"Drink about {liters} liters of water daily."