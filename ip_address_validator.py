# IP Address Validator
# COMP08101 Coursework
# B01817162

def validate_ip(ip):
    parts = ip.split(".")

    if len(parts) != 4:
        return False

    for part in parts:
        if not part.isdigit():
            return False

        number = int(part)

        if number < 0 or number > 255:
            return False

    return True


def classify_ip(ip):
    first_octet = int(ip.split(".")[0])

    if 1 <= first_octet <= 126:
        return "Class A"
    elif 128 <= first_octet <= 191:
        return "Class B"
    elif 192 <= first_octet <= 223:
        return "Class C"
    elif 224 <= first_octet <= 239:
        return "Class D (Multicast)"
    elif 240 <= first_octet <= 255:
        return "Class E (Reserved)"
    else:
        return "Unknown"


def main():
    while True:
        print("\n=== IP Address Validator ===")
        ip = input("Enter an IPv4 address (or 'q' to quit): ")

        if ip.lower() == "q":
            print("Program terminated.")
            break

        if validate_ip(ip):
            print("Valid IP Address")
            print("Classification:", classify_ip(ip))
        else:
            print("Invalid IP Address")


if __name__ == "__main__":
    main()
