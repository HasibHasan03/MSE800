import sys, os
sys.path.append(os.path.dirname(__file__))

from schema import init_db
import students, courses, lectures

def main_menu():
    while True:
        print("\n===== SCHOOL MANAGEMENT MENU =====")
        print("1. Manage Students")
        print("2. Manage Courses")
        print("3. Manage Lectures")
        print("0. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            student_menu()
        elif choice == "2":
            course_menu()
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
        print("1. Add Student")
        print("2. View Students")
        print("3. Edit Student")
        print("4. Delete Student")
        print("0. Back")
        choice = input("Enter choice: ")

        if choice == "1": students.add_student()
        elif choice == "2": students.view_students()
        elif choice == "3": students.edit_student()
        elif choice == "4": students.delete_student()
        elif choice == "0": break
        else: print("Invalid choice!")

def course_menu():
    while True:
        print("\n--- Course Menu ---")
        print("1. Add Course")
        print("2. View Courses")
        print("3. Edit Course")
        print("4. Delete Course")
        print("0. Back")
        choice = input("Enter choice: ")

        if choice == "1": courses.add_course()
        elif choice == "2": courses.view_courses()
        elif choice == "3": courses.edit_course()
        elif choice == "4": courses.delete_course()
        elif choice == "0": break
        else: print("Invalid choice!")

def lecture_menu():
    while True:
        print("\n--- Lecture Menu ---")
        print("1. Add Lecture")
        print("2. View Lectures")
        print("3. Edit Lecture")
        print("4. Delete Lecture")
        print("0. Back")
        choice = input("Enter choice: ")

        if choice == "1": lectures.add_lecture()
        elif choice == "2": lectures.view_lectures()
        elif choice == "3": lectures.edit_lecture()
        elif choice == "4": lectures.delete_lecture()
        elif choice == "0": break
        else: print("Invalid choice!")

if __name__ == "__main__":
    init_db()
    main_menu()
