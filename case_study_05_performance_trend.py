


print("===== STUDENT PERFORMANCE TREND ANALYSIS =====")

try:
    number_of_tests = int(input("Enter number of tests: "))

    if number_of_tests <= 0:
        print("Please enter at least one test.")

    else:
        marks = []

        for i in range(number_of_tests):
            while True:
                try:
                    mark = float(
                        input(f"Enter marks for Test {i + 1} (0-100): ")
                    )

                    if 0 <= mark <= 100:
                        marks.append(mark)
                        break
                    else:
                        print("Marks must be between 0 and 100.")

                except ValueError:
                    print("Please enter a valid number.")

        print("\n===== PERFORMANCE REPORT =====")

        for i in range(number_of_tests):
            print(f"Test {i + 1}: {marks[i]} marks")

        average = sum(marks) / number_of_tests
        print("Average Marks:", round(average, 2))

        if number_of_tests >= 2:
            if marks[-1] > marks[0]:
                print("Performance Trend: Improving")
            elif marks[-1] < marks[0]:
                print("Performance Trend: Declining")
            else:
                print("Performance Trend: Stable")
        else:
            print("Performance Trend: Need at least two tests.")

except ValueError:
    print("Please enter a valid whole number for the number of tests.")

print("=============================================")
