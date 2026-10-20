
# Case Study 3: Attendance Recovery Computation

REQUIRED_ATTENDANCE = 75

print("===== ATTENDANCE RECOVERY SYSTEM =====")

try:
    total_classes = int(input("Enter total classes held: "))
    attended_classes = int(input("Enter classes attended: "))

    if total_classes <= 0:
        print("Total classes must be greater than zero.")

    elif attended_classes < 0 or attended_classes > total_classes:
        print("Invalid number of attended classes.")

    else:
        percentage = attended_classes / total_classes * 100

        print("Current attendance:", round(percentage, 2), "%")

        if percentage >= REQUIRED_ATTENDANCE:
            print("Status: Attendance requirement satisfied.")
            print("Additional classes needed: 0")

        else:
            # Calculate the minimum classes to attend consecutively
            additional_classes = 0

            while (
                (attended_classes + additional_classes)
                / (total_classes + additional_classes) * 100
                < REQUIRED_ATTENDANCE
            ):
                additional_classes += 1

            print("Status: Attendance is below 75%.")
            print("Additional classes to attend:",
                  additional_classes)

except ValueError:
    print("Please enter whole numbers only.")

print("======================================")

