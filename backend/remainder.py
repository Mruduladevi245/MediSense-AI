import threading
import time
import schedule

reminders = []


def add_reminder(medicine, reminder_time):
    reminders.append({
        "medicine": medicine,
        "time": reminder_time
    })

    schedule.every().day.at(reminder_time).do(
        lambda: print(f"🔔 Reminder: Time to take {medicine}")
    )


def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)


def start_scheduler():
    thread = threading.Thread(target=run_scheduler)
    thread.daemon = True
    thread.start()


def get_reminders():
    return reminders