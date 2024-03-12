class Manage_Input:

    def input_students_info():
        num_students = int(input("Enter the number of students: "))
        students_info = []
        for i in range(num_students):
            stu_id = input(f"Enter student {i+1}'s ID: ")
            stu_name = input(f"Enter student {i+1}'s name: ")
            stu_dob = input(f"Enter student {i+1}'s date of birth: ")
            students_info.append((stu_id, stu_name, stu_dob))
        return students_info

    def input_courses_info():
        num_courses = int(input("Enter the number of courses: "))
        courses_info = []
        for j in range(num_courses):
            course_id = input(f"Enter course {j+1}'s ID: ")
            course_name = input(f"Enter course {j+1}'s name: ")
            courses_info.append((course_id, course_name))
        return courses_info
    
    def input_marks():
        stu_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")
        mark = float(input("Enter mark for the student: "))
        return stu_id, course_id, mark
