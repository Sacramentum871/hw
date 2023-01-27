class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = {}
        self.courses_in_progress = []
        self.courses_completed = []
        self.stud_avg_list = []

  
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'ошибка'       


    def __str__(self):
        progress = ''.join(self.courses_in_progress)
        completed = ''.join(self.courses_completed)
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредний балл: {self.stud_avg()}\nИзучаемые курсы: {progress}\nЗавершенные курсы: {completed}'


    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Не является студентом'
        if self.stud_avg() < other.stud_avg():
            return f'Средний балл у студента {other.name} - выше: {other.stud_avg()}. Он победил!'
        else:
            return f'Средний балл у студента {self.name} - выше: {self.stud_avg()}. Он победил!'


    def stud_avg(self):
        for course, score in self.grades.items():
            if course in self.courses_in_progress:
                result = round(sum(score)/len(score), 2)
                self.stud_avg_list.extend([result])
            else:
                self.stud_avg_list.extend(score)
                result = sum(score)/len(score)
                self.stud_avg_list.extend([result])
        return result


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.lec_avg_list = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Не является лектором'
        if self.lec_avg() < other.lec_avg():
            return f'Средний балл у лектора {other.name} - выше: {other.lec_avg()}. Он победил!'
        else:
            return f'Средний балл у лектора {self.name} - выше: {self.lec_avg()}. Он победил!'


    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\Средний балл: {self.lec_avg()}'


    def lec_avg(self):
        for course, score in self.grades.items():
            if course in self.courses_attached:
                result = round(sum(score)/len(score), 2)
                self.lec_avg_list.extend([result])
            else:
                self.lec_avg_list.extend(score)
                result = sum(score)/len(score)
                self.lec_avg_list.extend([result])
        return result


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)


    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'ошибка'


def student_course_average_score(student_list, course_name):
    student_avg_score = 0
    student_count = 0
    for students in student_list:
        if [course_name] == students.courses_in_progress:
           student_avg_score += students.stud_avg_list[0]
           student_count += 1
    avg = student_avg_score / student_count
    return f'В рамках курса {course_name} средний балл учащихся составляет: {avg}'


def lecturers_course_average_score(lecturer_list, course_name):
    lecturers_avg_score = 0
    lecturers_count = 0
    for lecturers in lecturer_list:
        if [course_name] == lecturers.courses_attached:
           lecturers_avg_score += lecturers.lec_avg_list[0]
           lecturers_count += 1
    avg = lecturers_avg_score / lecturers_count
    return f'В рамках курса {course_name} средний лекторов {avg}'


stud_1 = Student('Vicont', 'Jordan')
stud_1.courses_in_progress += ['Python']
stud_1.courses_completed += ['Git']

stud_2 = Student('Terrense', 'Steadman')
stud_2.courses_in_progress += ['Web']
stud_2.courses_completed += ['Git']

student_list = [stud_1, stud_2]


lec_1 = Lecturer('Was', 'Chick')
lec_1.courses_attached += ['Python']

lec_2 = Lecturer('Mark', 'Chelik')
lec_2.courses_attached += ['Web']

lecturer_list = [lec_1, lec_2]

rev_1 = Reviewer('Miles','Morales')

rev_2 = Reviewer('Jason','Bourne')

rev_1.rate_student(stud_1, 'Python', 7)
rev_1.rate_student(stud_1, 'Python', 3)
rev_1.rate_student(stud_1, 'Python', 9)

rev_1.rate_student(stud_2, 'Web', 1)
rev_1.rate_student(stud_2, 'Web', 6)
rev_1.rate_student(stud_2, 'Web', 4)

stud_1.rate_lecturer(lec_1, 'Python', 5)
stud_1.rate_lecturer(lec_1, 'Python', 1)
stud_1.rate_lecturer(lec_1, 'Python', 9)

stud_2.rate_lecturer(lec_2, 'Web', 7)
stud_2.rate_lecturer(lec_2, 'Web', 3)
stud_2.rate_lecturer(lec_2, 'Web', 1)

print('Проверяющие:\n')
print(rev_1)
print('\n')
print(rev_2)
print('\n')
print('Студенты:\n')
print(stud_1)
print('\n')
print(stud_2)
print('\n')
print(stud_1<stud_2)
print('\n')
print('Лекторат:\n')
print(lec_1)
print('\n')
print(lec_2)
print('\n')
print(lec_1<lec_2)
print('\n')
print(lecturers_course_average_score(lecturer_list, 'Python'))
print('\n')
print(lecturers_course_average_score(lecturer_list, 'Web'))
print('\n')
print(student_course_average_score(student_list, 'Python'))
print('\n')
print(student_course_average_score(student_list, 'Web'))

