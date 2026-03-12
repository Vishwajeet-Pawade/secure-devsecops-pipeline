import subprocess

def run_command(user_input):
    allowed_commands = ["date", "whoami", "pwd"]
    
    if user_input in allowed_commands:
        subprocess.run([user_input], check=True)
    else:
        print("Command not allowed")

command = input("Enter command: ")
run_command(command)
