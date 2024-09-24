from assistant_utils import speak

custom_commands = {}

def handle_custom_command(command):
    return custom_commands.get(command, "")

def add_custom_command(command, response):
    custom_commands[command] = response
    speak(f"Custom command '{command}' added.")
