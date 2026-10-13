# STUDENT MARKS MANAGEMENT SYSTEM
# Arrays are represented by Python lists.

student_names = []
student_marks = []


def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    try:
        mark = float(input("Enter student's mark (0-100): "))

        if mark < 0 or mark > 100:
            print("Mark must be between 0 and 100.")
            return

        student_names.append(name)
        student_marks.append(mark)
        print("Student added successfully!")

    except ValueError:
        print("Please enter a valid number.")


def display_students():
    if not student_names:
        print("No student records available.")
        return

    print("\n--- STUDENT RECORDS ---")
    for i in range(len(student_names)):
        print(
            f"{i + 1}. {student_names[i]} "
            f"- {student_marks[i]}/100"
        )


def calculate_average():
    if not student_marks:
        print("No marks available.")
        return

    average = sum(student_marks) / len(student_marks)
    print(f"Average mark: {average:.2f}")


def find_top_student():
    if not student_marks:
        print("No marks available.")
        return

    highest_index = student_marks.index(max(student_marks))
    print("Top student:", student_names[highest_index])
    print("Highest mark:", student_marks[highest_index])


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add student")
    print("2. Display students")
    print("3. Calculate average mark")
    print("4. Find top student")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        calculate_average()
    elif choice == "4":
        find_top_student()
    elif choice == "5":
        print("Thank you for using the system!")
        break
    else:
        print("Invalid choice. Please try again.")
