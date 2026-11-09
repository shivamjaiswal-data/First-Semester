
from datetime import datetime



# 1. PERSON BASE CLASS


class Person:

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")



# 2. STUDENT CLASS


class Student(Person):

    student_count = 0

    def __init__(self, name, age, email, student_id):
        super().__init__(name, age, email)

        self.student_id = student_id
        self.courses = []
        self.marks = {}
        self.attendance = {}
        self.fees_paid = 0

        Student.student_count += 1

    def enroll_course(self, course):

        if course in self.courses:
            print("Already enrolled in this course.")
            return

        if len(course.students) >= course.capacity:
            print("Course is full.")
            return

        self.courses.append(course)
        course.add_student(self)

        self.attendance[course.course_name] = {
            "present": 0,
            "total": 0
        }

        print(f"{self.name} enrolled in {course.course_name}")

    def mark_attendance(self, course_name, present):

        if course_name not in self.attendance:
            print("Student is not enrolled in this course.")
            return

        self.attendance[course_name]["total"] += 1

        if present:
            self.attendance[course_name]["present"] += 1

    def calculate_attendance(self, course_name):

        if course_name not in self.attendance:
            return 0

        data = self.attendance[course_name]

        if data["total"] == 0:
            return 0

        return (data["present"] / data["total"]) * 100

    def add_marks(self, course_name, marks):

        if not any(c.course_name == course_name for c in self.courses):
            print("Student is not enrolled in this course.")
            return

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return

        self.marks[course_name] = marks
        print("Marks added successfully.")

    def calculate_grade(self, course_name):

        marks = self.marks.get(course_name)

        if marks is None:
            return "Not Available"

        if marks >= 90:
            return "A+"
        elif marks >= 80:
            return "A"
        elif marks >= 70:
            return "B"
        elif marks >= 60:
            return "C"
        elif marks >= 40:
            return "D"
        else:
            return "F"

    def pay_fees(self, amount):

        if amount <= 0:
            print("Invalid payment amount.")
            return

        self.fees_paid += amount
        print(f"₹{amount} paid successfully.")

    def display_report(self):

        print("\n========== STUDENT REPORT ==========")

        self.display_details()

        print("Student ID:", self.student_id)
        print("Fees Paid:", self.fees_paid)

        print("\nEnrolled Courses:")

        for course in self.courses:
            print("-", course.course_name)

        print("\nAcademic Performance:")

        for course, marks in self.marks.items():
            print(
                course,
                "| Marks:", marks,
                "| Grade:", self.calculate_grade(course)
            )

        print("\nAttendance:")

        for course in self.attendance:
            print(
                course,
                ":", round(self.calculate_attendance(course), 2), "%"
            )


# ==========================================
# 3. TEACHER CLASS
# ==========================================

class Teacher(Person):

    def __init__(self, name, age, email, teacher_id, salary):
        super().__init__(name, age, email)

        self.teacher_id = teacher_id
        self.salary = salary
        self.assigned_courses = []

    def assign_course(self, course):

        if course in self.assigned_courses:
            print("Teacher is already assigned.")
            return

        self.assigned_courses.append(course)
        course.teacher = self

        print(
            f"{self.name} assigned to {course.course_name}"
        )

    def display_details(self):

        super().display_details()

        print("Teacher ID:", self.teacher_id)
        print("Salary:", self.salary)


# 4. COURSE CLASS


class Course:

    course_count = 0

    def __init__(self, course_id, course_name, capacity=30):

        self.course_id = course_id
        self.course_name = course_name
        self.capacity = capacity

        self.students = []
        self.teacher = None

        Course.course_count += 1

    def add_student(self, student):

        if student not in self.students:
            self.students.append(student)

    def display_course(self):

        print("\nCourse ID:", self.course_id)
        print("Course Name:", self.course_name)
        print("Capacity:", self.capacity)
        print("Enrolled Students:", len(self.students))

        if self.teacher:
            print("Teacher:", self.teacher.name)
        else:
            print("Teacher: Not Assigned")



# 5. UNIVERSITY CLASS


class University:

    def __init__(self, university_name):

        self.university_name = university_name

        self.students = {}
        self.teachers = {}
        self.courses = {}

    def add_student(self, student):

        if student.student_id in self.students:
            print("Student ID already exists.")
            return

        self.students[student.student_id] = student

        print("Student registered successfully.")

    def add_teacher(self, teacher):

        if teacher.teacher_id in self.teachers:
            print("Teacher ID already exists.")
            return

        self.teachers[teacher.teacher_id] = teacher

        print("Teacher registered successfully.")

    def add_course(self, course):

        if course.course_id in self.courses:
            print("Course ID already exists.")
            return

        self.courses[course.course_id] = course

        print("Course added successfully.")

    def search_student(self, student_id):

        student = self.students.get(student_id)

        if student:
            student.display_report()
        else:
            print("Student not found.")

    def display_all_students(self):

        print("\n========== STUDENT LIST ==========")

        if not self.students:
            print("No students registered.")
            return

        for student in self.students.values():
            print(
                student.student_id,
                student.name,
                student.email
            )

    def display_all_courses(self):

        print("\n========== COURSE LIST ==========")

        for course in self.courses.values():
            course.display_course()



# 6. MAIN APPLICATION


def main():

    university = University("IMCC University")

    # Creating students
    s1 = Student("Shivam", 22, "shivam@gmail.com", 101)
    s2 = Student("Rahul", 23, "rahul@gmail.com", 102)
    s3 = Student("Amit", 21, "amit@gmail.com", 103)

    university.add_student(s1)
    university.add_student(s2)
    university.add_student(s3)

    # Creating teachers
    t1 = Teacher(
        "Dr. Sharma", 40,
        "sharma@gmail.com", 201, 60000
    )

    t2 = Teacher(
        "Dr. Verma", 38,
        "verma@gmail.com", 202, 55000
    )

    university.add_teacher(t1)
    university.add_teacher(t2)

    # Creating courses
    c1 = Course(301, "Python Programming", 30)
    c2 = Course(302, "Data Structures", 25)
    c3 = Course(303, "Database Management", 20)

    university.add_course(c1)
    university.add_course(c2)
    university.add_course(c3)

    # Assigning teachers
    t1.assign_course(c1)
    t1.assign_course(c2)
    t2.assign_course(c3)

    # Enrolling students
    s1.enroll_course(c1)
    s1.enroll_course(c2)

    s2.enroll_course(c1)
    s2.enroll_course(c3)

    s3.enroll_course(c2)

    # Recording attendance
    s1.mark_attendance("Python Programming", True)
    s1.mark_attendance("Python Programming", True)
    s1.mark_attendance("Python Programming", False)

    s1.mark_attendance("Data Structures", True)
    s1.mark_attendance("Data Structures", True)

    # Adding marks
    s1.add_marks("Python Programming", 92)
    s1.add_marks("Data Structures", 85)

    s2.add_marks("Python Programming", 76)
    s2.add_marks("Database Management", 88)

    # Fee payments
    s1.pay_fees(25000)
    s2.pay_fees(20000)

    # Displaying reports
    university.display_all_students()
    university.display_all_courses()

    university.search_student(101)

    print("\nTotal Students:", Student.student_count)
    print("Total Courses:", Course.course_count)


if __name__ == "__main__":
    main()
