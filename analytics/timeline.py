from datetime import datetime


class Timeline:

    @staticmethod
    def create(reports):

        timeline = []

        reports = sorted(

            reports,

            key=lambda x: x["date"]

        )

        for report in reports:

            timeline.append({

                "date": report["date"],

                "report_type":
                report.get("type", "Medical Report"),

                "health_score":
                report.get("health_score", 0)

            })

        return timeline

    @staticmethod
    def latest(reports):

        if not reports:

            return None

        reports = sorted(

            reports,

            key=lambda x: x["date"],

            reverse=True

        )

        return reports[0]