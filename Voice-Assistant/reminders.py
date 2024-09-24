import threading
import time

from assistant_utils import speak

reminders = []

def set_reminder(time_str, message):
    reminder_time = time.strptime(time_str, "%H:%M")
    reminder_time_seconds = time.mktime(time.localtime()) + (reminder_time.tm_hour * 3600 + reminder_time.tm_min * 60)
    reminders.append((reminder_time_seconds, message))
    speak(f"Reminder set for {time_str}.")

def check_reminders():
    while True:
        current_time = time.mktime(time.localtime())
        for reminder in reminders:
            reminder_time, message = reminder
            if current_time >= reminder_time:
                speak(f"Reminder: {message}")
                reminders.remove(reminder)
        time.sleep(60)  # Check every minute
