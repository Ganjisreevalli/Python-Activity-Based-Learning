

PASS_MARK = 35
MAX_GRACE_MARKS = 5
NUMBER_OF_SUBJECTS = 5

marks = []80

print(" EXAMINATION RESULT SYSTEM ")


for i in range(NUMBER_OF_SUBJECTS):
    while True:
        try:
            mark = int(input(f"Enter marks for Subject {i + 1} (0-100): "))

            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Please enter marks between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")


failed_subjects = []

for i in range(NUMBER_OF_SUBJECTS):
    if marks[i] < PASS_MARK:
        failed_subjects.append(i)

grace_used = 0


if len(failed_subjects) == 1:
    index = failed_subjects[0]
    marks_needed = PASS_MARK - marks[index]

    if marks_needed <= MAX_GRACE_MARKS:
        marks[index] = PASS_MARK
        grace_used = marks_needed


total = sum(marks)
percentage = total / NUMBER_OF_SUBJECTS


print("\n========== RESULT ==========")

for i in range(NUMBER_OF_SUBJECTS):
    print(f"Subject {i + 1}: {marks[i]}")

print("Grace Marks Used:", grace_used)
print("Total Marks:", total, "/", NUMBER_OF_SUBJECTS * 100)
print("Percentage:", round(percentage, 2), "%")

if all(mark >= PASS_MARK for mark in marks):
    print("Final Result: PASS")
else:
    print("Final Result: FAIL")

print("============================")
