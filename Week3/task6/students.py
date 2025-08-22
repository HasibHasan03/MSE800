from db import execute_query, fetch_query

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    execute_query("INSERT INTO students (name, age) VALUES (?, ?)", (name, age))
    print("Student added successfully!")

def view_students():
    rows = fetch_query("SELECT * FROM students")
    for row in rows:
        print(row)

def edit_student():
    student_id = input("Enter student ID to edit: ")
    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    execute_query("UPDATE students SET name=?, age=? WHERE id=?", (name, age, student_id))
    print("Student updated successfully!")

def delete_student():
    student_id = input("Enter student ID to delete: ")
    execute_query("DELETE FROM students WHERE id=?", (student_id,))
    print("Student deleted successfully!")
