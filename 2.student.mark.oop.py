class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

class ManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self):
        num_students = int(input("Enter the number of students: "))
        for i in range(num_students):
            student_id = input("Enter student ID: ")
            student_name = input("Enter student name: ")
            student_dob = input("Enter student date of birth: ")
            student = Student(student_id, student_name, student_dob)
            self.students.append(student)

    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for i in range(num_courses):
            course_id = input("Enter course ID: ")
            course_name = input("Enter course name: ")
            course = Course(course_id, course_name)
            self.courses.append(course)

    def input_marks(self):
        course_id = input("Enter course ID: ")
        for course in self.courses:
            if course.id == course_id:
                for student in course.students:
                    mark = input(f"Enter mark for {student.name}: ")
                    student.marks[course_id] = mark

    def list_courses(self):
        print("List of courses:")
        for course in self.courses:
            print(course.id, course.name)

    def list_students(self):
        print("List of students:")
        for student in self.students:
            print(student.id, student.name)

    def show_marks(self):
        course_id = input("Enter course ID: ")
        for course in self.courses:
            if course.id == course_id:
                print(f"Marks for course {course.name}:")
                for student in course.students:
                    mark = student.marks.get(course_id, "N/A")
                    print(student.id, student.name, mark)

    def run(self):
        self.input_students()
        self.input_courses()

        while True:
            print("\nMenu:")
            print("1. Input marks")
            print("2. List courses")
            print("3. List students")
            print("4. Show student marks for a course")
            print("5. Quit")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.input_marks()
            elif choice == "2":
                self.list_courses()
            elif choice == "3":
                self.list_students()
            elif choice == "4":
                self.show_marks()
            elif choice == "5":
                break
            else:
                print("Invalid choice, please try again.")


if __name__ == '__main__':
    ms = ManagementSystem()
    ms.run()
