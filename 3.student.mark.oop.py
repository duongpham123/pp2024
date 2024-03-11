import numpy as np
import math

class Student:
    def __init__(self, stu_id, stu_name, stu_dob):
        self.stu_id = stu_id
        self.stu_name = stu_name
        self.stu_dob = stu_dob

class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

class Mark:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}
    def input_stu_inf(self):
        num_students = int(input("Enter the number of students: "))
        for i in range(num_students):
            stu_id = input(f"Enter student {i+1}'s ID: ")
            stu_name = input(f"Enter student {i+1}'s name: ")
            stu_dob = input(f"Enter student {i+1}'s date of birth: ")
            self.students.append(Student(stu_id, stu_name, stu_dob))

    def input_courses(self):
        print("--------------------------------")
        num_courses = int(input("Enter the number of courses: "))
        for j in range(num_courses):
            course_id = input(f"Enter course {j+1}'s ID: ")
            course_name = input(f"Enter course {j+1}'s name: ")
            self.courses.append(Course(course_id, course_name))
            
    def input_marks(self):
        print("--------------------------------")
        print("Enter student's marks")
        stu_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")
        mark = float(input("Enter mark for the student: "))
        
        if course_id not in self.marks:
            self.marks[course_id] = {}
        self.marks[course_id][stu_id] = mark

    def list_courses(self):
        print("--------------------------------")    
        print("List of courses:")
        for course in self.courses:
            print(f"Course ID: {course.course_id}, Course Name: {course.course_name}")
        print("--------------------------------")

    def list_stu(self):
        print("List of students:")
        print("---------------------------------------------")
        for student in self.students:
            print(f"|Student ID: {student.stu_id}| Student Name: {student.stu_name}| DoB: {student.stu_dob}|")
            print("---------------------------------------------")

    def round_down(self,mark):
        mark_round_down = math.floor(mark*10)/10
        return mark_round_down
    
    def calculate_average_gpa(self, stu_id):
        marks = [self.marks[course_id][stu_id] for course_id in self.marks if stu_id in self.marks[course_id]]
        if not marks:
            return 0
        return np.mean(marks)

    def weighted_sum_of_credits_and_marks(self, stu_id):
        marks = np.array([self.marks.get(course_id, {}).get(stu_id, 0) for course_id in self.marks])
        total_credits = len(self.marks) * 3  
        return np.sum(marks * 3), total_credits

    def sort_students_by_gpa(self):
        sorted_students = sorted(self.students, key=lambda student: self.calculate_average_gpa(student.stu_id), reverse=True)
        return sorted_students
    
    def show_stu_marks(self):
        print("--------------------------------")
        course_id = input("Enter course ID to show marks: ")
        if course_id in self.marks:
            print(f"Student marks for course {course_id}:")
            for stu_id, mark in self.marks[course_id].items():
                stu_name = next((student.stu_name for student in self.students if student.stu_id == stu_id), None)
                if stu_name:
                    print(f"Student ID: {stu_id}, Student Name: {stu_name}, Mark: {self.round_down(mark)}")
                else:
                    print(f"Student ID: {stu_id}, Mark: {self.round_down(mark)}")
        else:
            print(f"No marks are found for course {course_id}")

mark = Mark()
mark.input_stu_inf()
mark.input_courses()
mark.list_courses()
mark.list_stu()

while True:
    print("\nPress 1 to input marks")
    print("Press 2 to display student marks")
    print("Press 3 to sort students by GPA")
    print("Press 4 to quit")

    choice = input("Enter a number from 1 to 4: ")
    
    if choice == '1':
        mark.input_marks()
    elif choice == '2':
        mark.show_stu_marks()
    elif choice == '3':
        sorted_students = mark.sort_students_by_gpa()
        print("Students sorted by GPA:")
        for student in sorted_students:
            print(f"Student ID: {student.stu_id}, Student Name: {student.stu_name}, Average GPA: {mark.calculate_average_gpa(student.stu_id)}")
            print("--------------------------------")
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")