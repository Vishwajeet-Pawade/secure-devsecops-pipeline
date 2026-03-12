import subprocess

def run_command(user_input):
    subprocess.call(user_input)

command = input("Enter command: ")
run_command(command)

