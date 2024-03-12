import numpy as np

class Mark:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

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
