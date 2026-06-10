import json
from models.student import Student
from models.course import Course


class SchoolSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.registrations = {}

    def add_student(self):
        student_id = input("Student ID: ")
        name = input("Name: ")
        email = input("Email: ")
        phone = input("Phone: ")

        if student_id in self.students:
            print("Student already exists.")
            return

        self.students[student_id] = Student(
            student_id, name, email, phone
        )
        print("Student added.")

    def view_students(self):
        for student in self.students.values():
            print(student)

    def search_student(self):
        student_id = input("Enter Student ID: ")

        if student_id in self.students:
            print(self.students[student_id])
        else:
            print("Student not found.")

    def add_course(self):
        course_id = input("Course ID: ")
        course_name = input("Course Name: ")
        trainer = input("Trainer: ")
        capacity = int(input("Capacity: "))

        if course_id in self.courses:
            print("Course already exists.")
            return

        self.courses[course_id] = Course(
            course_id, course_name, trainer, capacity
        )
        print("Course added.")

    def view_courses(self):
        for course in self.courses.values():
            print(course)

    def register_student(self):
        student_id = input("Student ID: ")
        course_id = input("Course ID: ")

        if course_id not in self.registrations:
            self.registrations[course_id] = []

        if student_id in self.registrations[course_id]:
            print("Already registered.")
            return

        self.registrations[course_id].append(student_id)
        print("Registration successful.")

    def view_students_in_course(self):
        course_id = input("Course ID: ")

        if course_id in self.registrations:
            print("Students in course:")
            for student_id in self.registrations[course_id]:
                print(student_id)
        else:
            print("No students registered.")

    def view_courses_for_student(self):
        student_id = input("Student ID: ")
        found = False

        for course_id, students in self.registrations.items():
            if student_id in students:
                print(course_id)
                found = True

        if not found:
            print("No courses found.")

    def save_data(self):
        with open("data/registrations.json", "w") as file:
            json.dump(self.registrations, file)

    def load_data(self):
        try:
            with open("data/registrations.json", "r") as file:
                self.registrations = json.load(file)
        except FileNotFoundError:
            pass