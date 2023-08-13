from model.Lesson import Lesson
# from model.Student import Student
# from model.Teacher import Teacher
from data.DbManager import DbManager
import uuid


def add_new_lesson():
    try:
        lesson_id = str(uuid.uuid4())
        name = str(input("Please enter lesson name : "))
        teacher = str(input("OK, Please enter teacher name : "))
        DbManager.add_lesson(Lesson(lesson_id, name, teacher))
    except Exception as e:
        print(f"add_new_lesson() Error: {e}")


def add_new_student():
    try:
        lesson_id = str(uuid.uuid4())
        name = str(input("Please enter lesson name : "))
        teacher = str(input("OK, Please enter teacher name : "))
        DbManager.add_lesson(Lesson(lesson_id, name, teacher))
    except Exception as e:
        print(f"add_new_lesson() Error: {e}")


def main():
    print("\n+++++ Hello, Welcome to My App :) +++++\n\n")
    mode = int(input("Please select mode :\n1) Manage Lessons\n2) Manage Students\n3) Manage Teachers\n4) Create Database\n"))
    match mode:
        case 1:
            print("Adding Lesson to Database...")
            add_new_lesson()
        case 2:
            print("Hi Student")
        case 3:
            print("Hi Teacher")
        case 4:
             print("Creating Database...")
             DbManager.create_database()
        case _:
            print("Unknown Mode!")


if __name__ == "__main__":
    main()
