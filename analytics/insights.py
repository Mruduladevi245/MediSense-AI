class Insights:
    
    @staticmethod
    def generate(report):

        insights = []

        if float(report.get("Glucose", 90)) > 100:

            insights.append(
                "Blood glucose is slightly elevated. Reduce sugary foods."
            )

        if float(report.get("Cholesterol", 180)) > 200:

            insights.append(
                "High cholesterol detected. Consider a low-fat diet."
            )

        if float(report.get("Hemoglobin", 13)) < 12:

            insights.append(
                "Low hemoglobin detected. Increase iron-rich foods."
            )

        if float(report.get("BMI", 22)) > 25:

            insights.append(
                "BMI indicates overweight. Increase physical activity."
            )

        if not insights:

            insights.append(
                "All major parameters appear within normal range."
            )

        return insights