students = []
courses = []

def input_students():
    num_students = int(input("Enter the number of students: "))
    for i in range(num_students):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student date of birth: ")
        student = (student_id, student_name, student_dob, {})
        students.append(student)

def input_courses():
    num_courses = int(input("Enter the number of courses: "))
    for i in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        course = (course_id, course_name, {})
        courses.append(course)

def input_marks():
    course_id = input("Enter course ID: ")
    for course in courses:
        if course[0] == course_id:
            for student in students:
                mark = input(f"Enter mark for {student[1]}: ")
                course[2][student[0]] = mark

def list_courses():
    print("List of courses:")
    for course in courses:
        print(course[0], course[1])

def list_students():
    print("List of students:")
    for student in students:
        print(student[0], student[1])

def show_marks():
    course_id = input("Enter course ID: ")
    for course in courses:
        if course[0] == course_id:
            print(f"Marks for course {course[1]}:")
            for student in students:
                mark = course[2].get(student[0], "N/A")
                print(student[0], student[1], mark)

def main():
    input_students()
    input_courses()

    while True:
        print("\nMenu:")
        print("1. Input marks")
        print("2. List courses")
        print("3. List students")
        print("4. Show student marks for a course")
        print("5. Quit")

        choice = input("Enter your choice: ")
        if choice == "1":
            input_marks()
        elif choice == "2":
            list_courses()
        elif choice == "3":
            list_students()
        elif choice == "4":
            show_marks()
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()