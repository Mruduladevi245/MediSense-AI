class BMI:
    
    @staticmethod
    def calculate(weight, height):

        h = height / 100

        bmi = weight / (h * h)

        return round(bmi, 2)