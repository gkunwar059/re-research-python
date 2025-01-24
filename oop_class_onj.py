class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Courses:
    def __init__(self, name, max_student):
        self.name = name
        self.max_student = max_student
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_student:
            self.students.append(student)
            return True
        return {"error": "No space in this course"}

    def get_average_grade(self):
        pass
        return {
            "msg":"Average grade of the course is"
        }


s1 = Student("John", 20, 9.8)
s2 = Student("Rohan", 20, 9.8)
s3 = Student("JIbra", 20, 9.8)
print(f"The grade of the student whose name {s1.name}  is {s1.get_grade()}")

course = Courses("Science", max_student=2)
# course.add_student(s1)
# course.add_student(s2)
course.add_student(s3)
print(course.get_average_grade())
