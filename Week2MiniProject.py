# Lists to store patient records and appointments
patients = []
appointments = []

# Running counter for unique patient IDs and total revenue tracker
patient_counter = 1
total_revenue = 0

# Main loop to keep the system running until the receptionist exits
while True:
    print("\n--- HOSPITAL PATIENT AND APPOINTMENT MANAGEMENT SYSTEM ---")
    print("1. Register a new patient")
    print("2. View registered patients")
    print("3. Book an appointment")
    print("4. View appointments")
    print("5. Calculate patient bills")
    print("6. Search for a patient by ID")
    print("7. Cancel an appointment")
    print("8. View hospital summary (Total Patients & Revenue)")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")

    # 1. Register a new patient
    if choice == "1":
        name = input("Patient full name: ")
        age = int(input("Patient age: "))
        phone = input("Phone number: ")

        # Input validation for age
        if age <= 0:
            print("Error: Age must be greater than zero.")
        else:
            # Generate unique patient ID using running counter
            patient_id = "P" + str(patient_counter)
            patient_counter = patient_counter + 1

            # Store patient record as a list inside the main patients list
            patient_record = [patient_id, name, age, phone]
            patients.append(patient_record)

            print("Patient registered successfully! Assigned Patient ID:", patient_id)

    # 2. View registered patients
    elif choice == "2":
        print("\n--- REGISTERED PATIENTS ---")
        if len(patients) == 0:
            print("No patients registered yet.")
        else:
            for p in patients:
                print("ID:", p[0], "| Name:", p[1], "| Age:", p[2], "| Phone:", p[3])

    # 3. Book an appointment
    elif choice == "3":
        p_id = input("Enter Patient ID: ")

        # Check if patient ID exists
        patient_found = False
        for p in patients:
            if p[0] == p_id:
                patient_found = True

        if patient_found == False:
            print("Error: Patient ID not found. Please register the patient first.")
        else:
            department = input("Department (General consultation, Dental, Eye clinic, or Cardiology): ")

            # Validate department
            if department != "General consultation" and department != "Dental" and department != "Eye clinic" and department != "Cardiology":
                print("Error: Invalid department selected.")
            else:
                day = input("Appointment day (e.g., Monday): ")
                time = input("Appointment time (e.g., 10:00 AM): ")

                # Check for duplicate appointment slots and patient double-booking
                slot_taken = False
                patient_busy = False

                for app in appointments:
                    # Same department, day, and time = duplicate slot
                    if app[1] == department and app[2] == day and app[3] == time:
                        slot_taken = True
                    # Same patient, day, and time = patient booked twice at the same time
                    if app[0] == p_id and app[2] == day and app[3] == time:
                        patient_busy = True

                if slot_taken == True:
                    print("Error: That appointment slot is already booked in", department)
                elif patient_busy == True:
                    print("Error: This patient already has another appointment at that exact day and time.")
                else:
                    appointment_record = [p_id, department, day, time]
                    appointments.append(appointment_record)
                    print("Appointment booked successfully for", p_id, "in", department, "on", day, "at", time)

    # 4. View appointments
    elif choice == "4":
        print("\n--- SCHEDULED APPOINTMENTS ---")
        if len(appointments) == 0:
            print("No appointments scheduled yet.")
        else:
            for app in appointments:
                print("Patient ID:", app[0], "| Department:", app[1], "| Day:", app[2], "| Time:", app[3])

    # 5. Calculate patient bills
    elif choice == "5":
        p_id = input("Enter Patient ID to generate bill: ")

        # Find patient name
        patient_name = ""
        for p in patients:
            if p[0] == p_id:
                patient_name = p[1]

        if patient_name == "":
            print("Error: Patient ID not found.")
        else:
            department = input("Department visited (General consultation, Dental, Eye clinic, or Cardiology): ")

            if department == "General consultation":
                consultation_charge = 5000
            elif department == "Dental":
                consultation_charge = 10000
            elif department == "Eye clinic":
                consultation_charge = 8000
            elif department == "Cardiology":
                consultation_charge = 15000
            else:
                consultation_charge = 0
                print("Error: Invalid department.")

            if consultation_charge > 0:
                extra_charges = float(input("Additional service charges (enter 0 if none): "))

                if extra_charges < 0:
                    print("Error: Additional charges cannot be negative.")
                else:
                    total_bill = consultation_charge + extra_charges
                    total_revenue = total_revenue + consultation_charge

                    print("\n--- PATIENT BILL ---")
                    print("Patient ID:", p_id)
                    print("Patient Name:", patient_name)
                    print("Department:", department)
                    print("Consultation Charge:", consultation_charge)
                    print("Additional Charges:", extra_charges)
                    print("Total Amount Payable:", total_bill)

    # 6. Advanced Challenge: Search for a patient using their ID
    elif choice == "6":
        search_id = input("Enter Patient ID to search: ")
        found = False
        for p in patients:
            if p[0] == search_id:
                print("\n--- PATIENT RECORD FOUND ---")
                print("ID:", p[0], "| Name:", p[1], "| Age:", p[2], "| Phone:", p[3])
                found = True
        if found == False:
            print("No patient found with ID:", search_id)

    # 7. Advanced Challenge: Cancel an appointment
    elif choice == "7":
        cancel_id = input("Enter Patient ID to cancel appointment: ")
        cancel_day = input("Enter Appointment Day: ")
        cancel_time = input("Enter Appointment Time: ")

        cancelled = False
        for app in appointments:
            if app[0] == cancel_id and app[2] == cancel_day and app[3] == cancel_time:
                appointments.remove(app)
                cancelled = True
                print("Appointment cancelled successfully.")
                break

        if cancelled == False:
            print("Error: Matching appointment not found.")

    # 8. Advanced Challenge: Display total patients registered and total revenue
    elif choice == "8":
        print("\n--- HOSPITAL SUMMARY ---")
        print("Total Patients Registered:", len(patients))
        print("Total Consultation Revenue Generated:", total_revenue)

    # 9. Exit
    elif choice == "9":
        print("Exiting system. Goodbye!")
        break

    # Invalid menu option
    else:
        print("Invalid choice. Please select a number between 1 and 9.")