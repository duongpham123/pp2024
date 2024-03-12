import math
def round_down(mark):
    mark_round_down = math.floor(mark * 10) / 10
    return mark_round_down
class Manage_Output:
   
    def list_courses(courses):
        print("List of courses:")
        print("--------------------------------") 
        for course in courses:
            print(f"|Course ID: {course.course_id}|Course Name: {course.course_name}|")
        print("--------------------------------")
    
    def list_students(students):
        print("List of students:")
        print("---------------------------------------------")
        for student in students:
            print(f"|Student ID: {student.stu_id}| Student Name: {student.stu_name}| DoB: {student.stu_dob}|")
            print("---------------------------------------------")
    
    def show_student_marks(course_id, marks, students):
        print("--------------------------------")
        if course_id in marks:
            print(f"Student marks for course {course_id}:")
            for stu_id, mark in marks[course_id].items():
                stu_name = next((student.stu_name for student in students if student.stu_id == stu_id), None)
                mark_round_down = round_down(mark)
                if stu_name:
                    mark_round_down = math.floor(mark * 10) / 10
                    print("--------------------------------")
                    print(f"|Student ID: {stu_id}| Student Name: {stu_name}| Mark: {mark_round_down}|")
                    print("--------------------------------")
                else:
                    print("--------------------------------")
                    print(f"|Student ID: {stu_id}| Mark: {mark_round_down}|")
                    print("--------------------------------")
        else:
            print(f"No marks are found for course {course_id}")
    
    def display_sorted_students(sorted_students, mark):
        print("Students sorted by GPA:")
        for student in sorted_students:
            print(f"Student ID: {student.stu_id}, Student Name: {student.stu_name}, Average GPA: {mark.calculate_average_gpa(student.stu_id)}")
            print("--------------------------------")
