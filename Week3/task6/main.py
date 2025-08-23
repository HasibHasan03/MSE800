import sys, os
sys.path.append(os.path.dirname(__file__))

from schema import init_db
import students, courses, lectures

def main_menu():
    while True:
        print("\n===== SCHOOL MANAGEMENT MENU =====")
        print("1. Manage Admin")
        print("2. Manage Students")
        print("3. Manage Lectures")
        print("0. Exit")
        choice = input("Enter choice: ")

        if choice == "2":
            student_menu()
        elif choice == "1":
            admin_menu()
        elif choice == "3":
            lecture_menu()
        elif choice == "0":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

def student_menu():
    while True:
        print("\n--- Student Menu ---")
        # print("1. Add Student")
        print("2. View Students")
        # print("3. Edit Student")
        # print("4. Delete Student")
        print("0. Back")
        choice = input("Enter choice: ")

        if choice == "2": students.add_student()
        # elif choice == "2": students.view_students()
        # elif choice == "3": students.edit_student()
        # elif choice == "4": students.delete_student()
        elif choice == "0": break
        else: print("Invalid choice!")

def admin_menu():
    while True:
        print("\n--- Student Menu ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Edit Student")
        print("4. Delete Student")
        print("\n--- Course Menu ---")
        print("5. Add Course")
        print("6. View Courses")
        print("7. Edit Course")
        print("8. Delete Course")
        print("\n--- Lecture Menu ---")
        print("9. Add Lecture")
        print("10. View Lectures")
        print("11. Edit Lecture")
        print("12. Delete Lecture")

        print("0. Back")
        choice = input("Enter choice: ")

        if choice == "1": students.add_student()
        elif choice == "2": students.view_students()
        elif choice == "3": students.edit_student()
        elif choice == "4": students.delete_student()
        elif choice == "5": courses.add_course()
        elif choice == "6": courses.view_courses()
        elif choice == "7": courses.edit_course()
        elif choice == "8": courses.delete_course()
        elif choice == "9": lectures.add_lecture()
        elif choice == "10": lectures.view_lectures()
        elif choice == "11": lectures.edit_lecture()
        elif choice == "12": lectures.delete_lecture()
        elif choice == "0": break
        else: print("Invalid choice!")

def lecture_menu():
    while True:
        print("\n--- Lecture Menu ---")
        print("2. View Lectures")
        print("0. Back")
        choice = input("Enter choice: ")

        if choice == "2": lectures.add_lecture()
        # elif choice == "2": lectures.view_lectures()
        # elif choice == "3": lectures.edit_lecture()
        # elif choice == "4": lectures.delete_lecture()
        elif choice == "0": break
        else: print("Invalid choice!")

if __name__ == "__main__":
    init_db()
    main_menu()
