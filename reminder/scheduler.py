import schedule
import time


class ReminderScheduler:

    @staticmethod
    def add_job(time_string, message):

        schedule.every().day.at(time_string).do(
            lambda: print(message)
        )

    @staticmethod
    def start():

        while True:

            schedule.run_pending()

            time.sleep(1)