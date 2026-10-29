


print("===== NUMERIC PATTERN GENERATOR =====")

try:
    rows = int(input("Enter the number of rows (1-10): "))

    if rows < 1 or rows > 10:
        print("Please enter a number between 1 and 10.")

    else:
        print("\nGenerated Number Pattern:\n")

        for i in range(1, rows + 1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()

        print("\nPattern generated successfully!")

except ValueError:
    print("Invalid input. Please enter a whole number.")

print("=====================================")
