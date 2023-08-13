from model.Lesson import Lesson
import sqlite3

class DbManager:

    # def __init__(self) -> None:
    #     ...

    # Create database and tables
    @staticmethod
    def create_database():
        try:
            # Connect to sqlite database
            conn = sqlite3.connect('data/data.db')
            # cursor object
            cursor = conn.cursor()
            # drop query
            cursor.execute("DROP TABLE IF EXISTS LESSON")
            # create query
            query = """CREATE TABLE LESSON(
                    LESSON_ID TEXT NOT NULL,
                    NAME CHAR(30) NOT NULL, 
                    TEACHER CHAR(30) NOT NULL )"""
            cursor.execute(query)
            # drop query
            cursor.execute("DROP TABLE IF EXISTS STUDENT")
            # create query
            query = """CREATE TABLE STUDENT(
                    ID INTEGER PRIMARY KEY NOT NULL,
                    STUDENT_ID INTEGER NOT NULL,
                    FNAME CHAR(30) NOT NULL, 
                    LNAME CHAR(30) NOT NULL,
                    LESSONS TEXT NOT NULL )"""
            cursor.execute(query)
            # drop query
            cursor.execute("DROP TABLE IF EXISTS TEACHER")
            # create query
            query = """CREATE TABLE TEACHER(
                    ID INTEGER PRIMARY KEY NOT NULL,
                    TEACHER_ID INTEGER NOT NULL,
                    FNAME CHAR(30) NOT NULL, 
                    LNAME CHAR(30) NOT NULL )"""
            cursor.execute(query)
            # commit and close
            conn.commit()
            cursor.close()
            print("Database created successfully.")

        except sqlite3.Error as e:
            print(f"SQLite Error: {e}")
        finally:
            if conn:
                conn.close()
                print("Connection is closed.")

    @staticmethod
    def add_lesson(lesson: Lesson) -> None:
        try:
            conn = sqlite3.connect('data/data.db')
            cursor = conn.cursor()
            query = ('INSERT INTO LESSON (LESSON_ID,NAME,TEACHER) VALUES (:LESSON_ID, :NAME, :TEACHER);')
            
            params = {
                'LESSON_ID': lesson.lesson_id,
                'NAME': lesson.name,
                'TEACHER': lesson.teacher_name
            }
            conn.execute(query, params)
            conn.commit()
            cursor.close()
        except sqlite3.Error as e:
            print(f"add_lesson() SQLite Error: {e}")
        finally:
            if conn:
                conn.close()
                print("OK, Lesson Added Success.")

