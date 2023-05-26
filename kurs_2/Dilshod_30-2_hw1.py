class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        marital_status = "женат" if self.is_married else "холост"
        print(f"Привет, меня зовут {self.fullname}. Мне {self.age} лет и я {marital_status}.")


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        if isinstance(marks, dict):
            if len(marks) > 3:
                raise ValueError("Слишком много предметов")
        self.marks = marks

    def calculate_average_grade(self):
        sum_of_grades = sum(self.marks.values())
        num_of_subjects = len(self.marks)
        average_grade = sum_of_grades / num_of_subjects
        return average_grade


class Teacher(Person):
    salary = 20000

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        standard_salary = self.salary
        if self.experience > 3:
            bonus_percentage = (self.experience - 3) * 0.05
            bonus_amount = standard_salary * bonus_percentage
            total_salary = standard_salary + bonus_amount
        else:
            total_salary = standard_salary
        return total_salary


def create_students():
    students = []
    student_a = Student("Petrov Petr", 16, False, {"Математика": 85, "Физика": 92, "Химия": 78})
    student_b = Student("Mamyrov Usen", 15, False, {"Математика": 67, "Физика": 87, "Химия": 74})
    student_c = Student("Volodin V", 16, False, {"Математика": 85, "Физика": 98, "Химия": 70})

    students.append(student_a)
    students.append(student_b)
    students.append(student_c)

    return students


students_list = create_students()

for student in students_list:
    student.introduce_myself()
    print("Оценки по предметам:")
    for subject, grade in student.marks.items():
        print(f"{subject}: {grade}")

    average_grade = student.calculate_average_grade()
    print(f"Средняя оценка: {average_grade}")
    print()
