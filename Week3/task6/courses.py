from db import execute_query, fetch_query

def add_course():
    title = input("Enter course title: ")
    description = input("Enter course description: ")
    execute_query("INSERT INTO courses (title, description) VALUES (?, ?)", (title, description))
    print("Course added!")

def view_courses():
    rows = fetch_query("SELECT * FROM courses")
    for row in rows:
        print(row)

def edit_course():
    view_courses()
    course_id = int(input("Enter course ID to edit: "))
    new_title = input("Enter new title: ")
    new_desc = input("Enter new description: ")
    execute_query("UPDATE courses SET title=?, description=? WHERE id=?", (new_title, new_desc, course_id))
    print("Course updated!")

def delete_course():
    view_courses()
    course_id = int(input("Enter course ID to delete: "))
    execute_query("DELETE FROM courses WHERE id=?", (course_id,))
    print("Course deleted!")
