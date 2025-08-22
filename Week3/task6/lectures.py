from db import execute_query, fetch_query
from courses import view_courses

def add_lecture():
    view_courses()
    course_id = int(input("Enter course ID for this lecture: "))
    topic = input("Enter lecture topic: ")
    execute_query("INSERT INTO lectures (course_id, topic) VALUES (?, ?)", (course_id, topic))
    print("Lecture added!")

def view_lectures():
    rows = fetch_query("""
        SELECT lectures.id, courses.title, lectures.topic 
        FROM lectures 
        JOIN courses ON lectures.course_id = courses.id
    """)
    for row in rows:
        print(row)

def edit_lecture():
    view_lectures()
    lecture_id = int(input("Enter lecture ID to edit: "))
    new_topic = input("Enter new topic: ")
    execute_query("UPDATE lectures SET topic=? WHERE id=?", (new_topic, lecture_id))
    print("Lecture updated!")

def delete_lecture():
    view_lectures()
    lecture_id = int(input("Enter lecture ID to delete: "))
    execute_query("DELETE FROM lectures WHERE id=?", (lecture_id,))
    print("Lecture deleted!")
