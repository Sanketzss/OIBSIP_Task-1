from assistant_utils import listen, speak, get_weather, get_time_date, search_wikipedia, search_google
from custom_commands import handle_custom_command, add_custom_command
from email_utils import send_email
from reminders import set_reminder, check_reminders
import threading


def main():
    speak("Hello, I'm your assistant. How can I assist you today?")

    while True:
        command = listen()

        if command is None:
            continue

        if "time" in command or "date" in command:
            get_time_date(command)

        elif "weather" in command:
            speak("Please tell me the city name.")
            city = listen()
            if city:
                get_weather(city)

        elif "wikipedia" in command:
            speak("What do you want to search for on Wikipedia?")
            topic = listen()
            if topic:
                search_wikipedia(topic)

        elif "google" in command:
            speak("What should I search for on Google?")
            query = listen()
            if query:
                search_google(query)

        elif "email" in command:
            speak("To whom should I send the email?")
            to_email = listen()
            speak("What is the subject?")
            subject = listen()
            speak("What should the message say?")
            message = listen()
            if to_email and subject and message:
                send_email(to_email, subject, message)

        elif "set reminder" in command:
            speak("What time should I set the reminder for? Please provide the time in HH:MM format.")
            time_str = listen()
            speak("What is the reminder for?")
            message = listen()
            if time_str and message:
                set_reminder(time_str, message)

        elif "add custom command" in command:
            speak("What should be the custom command?")
            custom_command = listen()
            speak("What should the response be?")
            custom_response = listen()
            if custom_command and custom_response:
                add_custom_command(custom_command, custom_response)

        elif command in handle_custom_command(command):
            response = handle_custom_command(command)
            speak(response)

        elif "stop" in command or "exit" in command:
            speak("Goodbye! Have a great day.")
            break

        else:
            speak("I didn't understand that. Please try again.")


if __name__ == "__main__":
    reminder_thread = threading.Thread(target=check_reminders)
    reminder_thread.daemon = True
    reminder_thread.start()

    main()
