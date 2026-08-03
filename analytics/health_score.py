class HealthScore:
    
    NORMAL_RANGES = {
        "Hemoglobin": (12.0, 17.5),
        "WBC": (4000, 11000),
        "Platelets": (150000, 450000),
        "Glucose": (70, 100),
        "Cholesterol": (0, 200),
        "BMI": (18.5, 24.9)
    }

    @classmethod
    def calculate(cls, report):

        score = 100
        remarks = []

        for parameter, normal in cls.NORMAL_RANGES.items():

            if parameter not in report:
                continue

            value = float(report[parameter])

            low, high = normal

            if value < low:

                score -= 5
                remarks.append(
                    f"{parameter} is below normal."
                )

            elif value > high:

                score -= 5
                remarks.append(
                    f"{parameter} is above normal."
                )

        score = max(score, 0)

        if score >= 90:
            status = "Excellent"

        elif score >= 75:
            status = "Good"

        elif score >= 60:
            status = "Average"

        else:
            status = "Poor"

        return {
            "score": score,
            "status": status,
            "remarks": remarks
        }