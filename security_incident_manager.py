# Security Incident Manager
# COMP08101 Coursework
# B01817162

incidents = []

while True:
    print("\n=== Security Incident Manager ===")
    print("1. Add Incident")
    print("2. View Incidents")
    print("3. Search Incident")
    print("4. Delete Incident")
    print("5. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        incident_id = input("Enter Incident ID: ")
        incident_type = input("Enter Incident Type: ")
        severity = input("Enter Severity Level: ")

        incident = {
            "ID": incident_id,
            "Type": incident_type,
            "Severity": severity
        }

        incidents.append(incident)
        print("Incident added successfully.")

    elif choice == "2":
        if len(incidents) == 0:
            print("No incidents recorded.")
        else:
            print("\nRecorded Incidents:")
            for incident in incidents:
                print(
                    f"ID: {incident['ID']}, "
                    f"Type: {incident['Type']}, "
                    f"Severity: {incident['Severity']}"
                )

    elif choice == "3":
        search_id = input("Enter Incident ID to search: ")

        found = False

        for incident in incidents:
            if incident["ID"] == search_id:
                print("\nIncident Found:")
                print(f"ID: {incident['ID']}")
                print(f"Type: {incident['Type']}")
                print(f"Severity: {incident['Severity']}")
                found = True
                break

        if not found:
            print("Incident not found.")

    elif choice == "4":
        delete_id = input("Enter Incident ID to delete: ")

        found = False

        for incident in incidents:
            if incident["ID"] == delete_id:
                incidents.remove(incident)
                print("Incident deleted successfully.")
                found = True
                break

        if not found:
            print("Incident not found.")

    elif choice == "5":
        print("Exiting Security Incident Manager...")
        break

    else:
        print("Invalid option. Please try again.")
