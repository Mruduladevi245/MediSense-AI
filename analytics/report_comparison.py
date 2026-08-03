class ReportComparison:
    
    @staticmethod
    def compare(old_report, new_report):

        comparison = {}

        parameters = set(old_report.keys()) | set(new_report.keys())

        for parameter in parameters:

            old = float(old_report.get(parameter, 0))

            new = float(new_report.get(parameter, 0))

            difference = round(new - old, 2)

            if difference > 0:
                trend = "Increased"

            elif difference < 0:
                trend = "Decreased"

            else:
                trend = "No Change"

            comparison[parameter] = {

                "previous": old,

                "current": new,

                "difference": difference,

                "trend": trend

            }

        return comparison