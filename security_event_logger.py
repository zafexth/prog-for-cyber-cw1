# Security Event Logger
# COMP08101 Coursework

from datetime import datetime

CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "Cyber123"

event_id = 1

while True:
    username = input("Enter username: ")
    password = input("Enter password: ")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        status = "Success"

        print("\n--- Security Event Log ---")
        print(f"Event ID: {event_id}")
        print(f"Username: {username}")
        print("Event Type: Login Attempt")
        print(f"Timestamp: {timestamp}")
        print(f"Status: {status}")

        print("\nAccess Granted")
        break

    else:
        status = "Failure"

        print("\n--- Security Event Log ---")
        print(f"Event ID: {event_id}")
        print(f"Username: {username}")
        print("Event Type: Login Attempt")
        print(f"Timestamp: {timestamp}")
        print(f"Status: {status}")

        print("\nInvalid credentials. Try again.")

    event_id += 1
