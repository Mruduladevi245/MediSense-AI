class SleepReminder:
    
    @staticmethod
    def recommendation(age):

        if age < 18:

            return "Sleep 8–10 hours."

        elif age < 65:

            return "Sleep 7–9 hours."

        return "Sleep 7–8 hours."