from input import Manage_Input
from output import Manage_Output
from domains.student import Student
from domains.course import Course
from domains.mark import Mark

manage_output = Manage_Output
mark = Mark()
mark.students = [Student(*info) for info in Manage_Input.input_students_info()]
mark.courses = [Course(*info) for info in Manage_Input.input_courses_info()]

manage_output.list_courses(mark.courses)
manage_output.list_students(mark.students)



    
while True:
    print("\nPress 1 to input marks")
    print("Press 2 to display student marks")
    print("Press 3 to sort students by GPA")
    print("Press 4 to quit")

    choice = input("Enter a number from 1 to 4: ")
    
    if choice == '1':
        stu_id, course_id, mark_val = Manage_Input.input_marks()
        if course_id not in mark.marks:
            mark.marks[course_id] = {}
        mark.marks[course_id][stu_id] = mark_val
    elif choice == '2':
        course_id = input("Enter course ID to show marks: ")
        manage_output.show_student_marks(course_id, mark.marks, mark.students)
    elif choice == '3':
        sorted_students = mark.sort_students_by_gpa()
        manage_output.display_sorted_students(sorted_students, mark)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
