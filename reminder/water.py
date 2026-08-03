class WaterReminder:
    
    @staticmethod
    def daily_goal(weight):

        liters = round(weight * 0.035, 1)

        return {

            "daily_goal_liters": liters,

            "cups": round((liters * 1000) / 250)

        }