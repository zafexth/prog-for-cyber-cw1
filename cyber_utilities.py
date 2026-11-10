# Cyber Security Utilities
# COMP08101 Coursework
# B01817162

def password_strength_checker():
    password = input("Enter a password: ")

    score = 0

    if len(password) >= 8:
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(not char.isalnum() for char in password):
        score += 1

    if score <= 2:
        print("Weak Password")
    elif score <= 4:
        print("Moderate Password")
    else:
        print("Strong Password")


def caesar_cipher():
    text = input("Enter text to encrypt: ")
    shift = int(input("Enter shift value: "))

    encrypted = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - start + shift) % 26 + start)
        else:
            encrypted += char

    print("Encrypted text:", encrypted)


def port_scanner():
    common_ports = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        443: "HTTPS"
    }

    print("\nCommon Ports:")
    for port, service in common_ports.items():
        print(f"Port {port}: {service}")


def main():
    while True:
        print("\n=== Cyber Security Utilities ===")
        print("1. Password Strength Checker")
        print("2. Caesar Cipher Encryptor")
        print("3. Common Port Viewer")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            password_strength_checker()

        elif choice == "2":
            caesar_cipher()

        elif choice == "3":
            port_scanner()

        elif choice == "4":
            print("Exiting Cyber Security Utilities...")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
