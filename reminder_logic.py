import time
from datetime import datetime
from notifier import send_notification
import config

def start_reminder_loop():
    """
    Runs an infinite loop that sends a hydration reminder every config.INTERVAL_MINUTES.
    """

    interval_sec = config.INTERVAL_MINUTES*60
    print(f"[WaterBuddy] Started - will remind every {config.INTERVAL_MINUTES}min")

    while True:

        time.sleep(interval_sec)

        now = datetime.now().strftime("%H:%M")
        message= f"{config.MESSAGE}\n(Current time: {now})"
        send_notification(config.TITLE, message)
        print(f"[WaterBuddy] Reminder sent at {now}")