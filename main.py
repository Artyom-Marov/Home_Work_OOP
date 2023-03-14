class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)
           
    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def average_rating(self):
        value = []
        for v in self.grades.values():
            value += v
        rating = round(sum(value) / len(value))
        return rating
        
    def __str__(self):
        in_progress = ', '.join(self.courses_in_progress)
        finished = ', '.join(self.finished_courses)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_rating()}\nКурсы в процессе изучения: {in_progress}\nЗавершенные курсы: {finished}'
        return res
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            print(f'Ошибка! Разные классы.')
            return
        return self.average_rating() < other.average_rating()
    
    def __le__(self, other):
        if not isinstance(other, Student):
            print(f'Ошибка! Разные классы.')
            return
        return self.average_rating() <= other.average_rating()
    
    def __eq__(self, other):
        if not isinstance(other, Student):
            print(f'Ошибка! Разные классы.')
            return
        return self.average_rating() == other.average_rating()

    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        
    def average_rating(self):
        value = []
        for v in self.grades.values():
            value += v
        rating = round(sum(value) / len(value))
        return rating
        
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating()}'
        return res
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print(f'Ошибка! Разные классы.')
            return
        return self.average_rating() < other.average_rating()
    
    def __le__(self, other):
        if not isinstance(other, Lecturer):
            print(f'Ошибка! Разные классы.')
            return
        return self.average_rating() <= other.average_rating()
    
    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print(f'Ошибка! Разные классы.')
            return
        return self.average_rating() == other.average_rating()
        
    
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

        
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Git']

best_student2 = Student('Sidor', 'Sidorov', 'your_gender')
best_student2.courses_in_progress += ['OOP']
best_student2.finished_courses += ['Python', 'Git']
 
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer2 = Reviewer('Petr', 'Petrov')
cool_reviewer2.courses_attached += ['OOP']

cool_lecturer = Lecturer('Ivan', 'Ivanov')
cool_lecturer.courses_attached += ['Python']

cool_lecturer2 = Lecturer('Stepan', 'Stepanov')
cool_lecturer2.courses_attached += ['OOP']

best_student.rate_lecture(cool_lecturer, 'Python', 5)
best_student2.rate_lecture(cool_lecturer2, 'OOP', 10)
 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer2.rate_hw(best_student2, 'OOP', 7)

best_student.add_courses('Введение в Python')
best_student2.add_courses('Введение в Python')
 

print(cool_reviewer)
print(cool_lecturer)
print(best_student)

print(cool_reviewer2)
print(cool_lecturer2)
print(best_student2)

print(cool_lecturer > cool_lecturer2)
print(cool_lecturer <= cool_lecturer2)
print(cool_lecturer == cool_lecturer2)
print(f'Средняя оценка первого лектора: {cool_lecturer.average_rating()}')
print(f'Средняя оценка второго лектора: {cool_lecturer2.average_rating()}')
print(best_student < best_student2)
print(best_student >= best_student2)
print(best_student == best_student2)
print(f'Средняя оценка первого студента: {best_student.average_rating()}')
print(f'Средняя оценка второго студента: {best_student2.average_rating()}')


def average_rating_for_students(students, course):
    all_ratings = []
    for student in students:
        if student.grades.get(course):
            all_ratings += student.grades[course]    
    average_rating_in_course_for_students = round(sum(all_ratings) / len(all_ratings))
    return average_rating_in_course_for_students

def average_rating_for_lecturer(lecturers, course):
    all_ratings = []
    for lecturer in lecturers:
        if lecturer.grades.get(course):
            all_ratings += lecturer.grades[course]    
    average_rating_in_course_for_lecturer = round(sum(all_ratings) / len(all_ratings))
    return average_rating_in_course_for_lecturer
                                                  
    
print(average_rating_for_students([best_student, best_student2], 'Python'))
print(average_rating_for_students([cool_lecturer, cool_lecturer2], 'Python'))