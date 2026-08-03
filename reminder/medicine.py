from datetime import datetime


class MedicineReminder:

    def __init__(self):
        self.reminders = []

    def add_reminder(
        self,
        medicine,
        dosage,
        time,
        frequency
    ):

        reminder = {

            "medicine": medicine,

            "dosage": dosage,

            "time": time,

            "frequency": frequency,

            "created_at": datetime.now().isoformat(),

            "status": "Pending"

        }

        self.reminders.append(reminder)

        return reminder

    def list_reminders(self):

        return self.reminders

    def mark_taken(self, medicine):

        for reminder in self.reminders:

            if reminder["medicine"] == medicine:

                reminder["status"] = "Taken"

                return reminder

        return None