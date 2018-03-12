#Defining an array for students
students = []

def get_student_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student.title()
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_student_titlecase()
    print(students_titlecase)


def add_student(name, student_id=3230):
    sudent = {"name: name", "student_id: student_id"}
    students.append(student)


student_list = get_student_titlecase()


add_student("Mark")