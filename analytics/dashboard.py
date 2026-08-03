from analytics.health_score import HealthScore
from analytics.insights import Insights
from analytics.statistics import Statistics
from analytics.trend_analysis import TrendAnalysis


class Dashboard:

    @staticmethod
    def generate(report, history=None):

        if history is None:
            history = []

        health = HealthScore.calculate(report)

        insights = Insights.generate(report)

        glucose_history = []

        cholesterol_history = []

        for item in history:

            glucose_history.append(
                float(item.get("Glucose", 0))
            )

            cholesterol_history.append(
                float(item.get("Cholesterol", 0))
            )

        dashboard = {

            "health_score": health,

            "insights": insights,

            "statistics": {

                "glucose":
                Statistics.summary(glucose_history),

                "cholesterol":
                Statistics.summary(cholesterol_history)

            },

            "trends": {

                "glucose":
                TrendAnalysis.analyze(glucose_history),

                "cholesterol":
                TrendAnalysis.analyze(cholesterol_history)

            }

        }

        return dashboard