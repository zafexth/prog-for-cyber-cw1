# Security Tool
# COMP08101 Coursework
# B01817162

CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "Cyber123"


def login_authentication():
    attempts = 0

    while attempts < 3:
        username = input("Username: ")
        password = input("Password: ")

        if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
            print("Login successful.")
            return True

        attempts += 1
        print("Invalid credentials.")

    print("Account frozen for 24 hours.")
    return False


def security_event_counter():
    incorrect = 0
    total = 10

    print("\nSecurity Event Counter")

    for i in range(total):
        password = input(f"Attempt {i + 1}/10 - Enter password: ")

        if password != CORRECT_PASSWORD:
            incorrect += 1

    percentage = (incorrect / total) * 100

    print(f"\nIncorrect attempts: {incorrect}")
    print(f"Incorrect percentage: {percentage:.2f}%")

    if percentage > 50:
        print("ALERT: High number of incorrect password attempts!")


def brute_force_simulation():
    max_attempts = 5

    print("\nBrute Force Simulation")

    for attempt in range(1, max_attempts + 1):
        password = input(f"Attempt {attempt}: ")

        if password == CORRECT_PASSWORD:
            print("Password cracked successfully!")
            return

    print("Maximum attempts reached.")


def menu():
    while True:
        print("\n=== Security Tool ===")
        print("1. Security Event Counter")
        print("2. Brute-Force Simulation")
        print("3. Login Authentication")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            security_event_counter()

        elif choice == "2":
            brute_force_simulation()

        elif choice == "3":
            login_authentication()

        elif choice == "4":
            print("Thank you for using the security tool")
            break

        else:
            print("Invalid option.")


if login_authentication():
    menu()
