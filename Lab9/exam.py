import numpy as np
import os
import json

class ExamResult:
    def __init__(self, course_code, date, grade_limits):
        self.course_code = course_code
        self.date = date
        self.grade_limits = grade_limits
        self.student_dict = {}
        self.stats_dict = {}
        self.grade_list = ['U', '3', '4', '5']

    def grade_from_score(self, score):
        for i, grade_limit in enumerate(self.grade_limits):
            if score < grade_limit:
                return self.grade_list[i]
        return '5'

    def add_result(self, student_id, score):
        self.student_dict[student_id] = int(score)

    def get_result(self, student_id):
        if student_id in self.student_dict:
            return (self.student_dict[student_id], self.grade_from_score(self.student_dict[student_id]))
        return None

    def students(self):
        return sorted(list(self.student_dict.keys()))

    def students_highest_score(self):
        if len(self.student_dict) > 0:
            max_value = max(self.student_dict.values())
            return sorted([student for student, score in self.student_dict.items() if score == max_value])
        return []

    def statistics(self):
        for grade in self.grade_list:
            s_with_grade = 0
            for student in self.students():
                if self.get_result(student)[1] == grade:
                    s_with_grade += 1
            self.stats_dict[grade] = (f'{s_with_grade:2d}', f'{(s_with_grade/len(self.students()))*100:.0f}')

    def print_results(self):
        print('# Exam Information')
        print(f'Course code: {self.course_code}')
        print(f'Date: {self.date}\n')
        print('# Grades')

        for student in self.students():
            print(student, ': ', f'{self.get_result(student)[0]} {self.get_result(student)[1]}')
        
        self.statistics()
        print('\n# Grade Statistics')
        for grade in self.grade_list:
            print(f'{grade}: {self.stats_dict[grade][0]} ({self.stats_dict[grade][1]}%)')
        
    def write_to_json_file(self, filename):
        out_dict = {
            'course_code': self.course_code,
            'date': self.date,
            'grade_limits': self.grade_limits,
            'scores': self.student_dict
            }
        
        filepath = os.path.join(os.path.dirname(__file__), filename)
        with open(filepath, 'w') as json_file:
            json.dump(out_dict, json_file, indent=4)


def read_from_json_file(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath) as json_file:
        in_dict = json.load(json_file)
    
    tenta = ExamResult(in_dict['course_code'], in_dict['date'], in_dict['grade_limits'])
    for key, value in in_dict['scores'].items():
        tenta.add_result(key, value)

    return tenta


tenta = ExamResult('EDAA70', '2021', [15, 20, 30])

student_results = {}
samples = np.random.default_rng().normal(25, 10, 100)
scores = [max(0, min(40, round(x))) for x in samples]

for i, score in enumerate(scores):
    student_id = f'S{i:02d}'
    student_results[student_id] = score

for key, value in student_results.items():
    tenta.add_result(key, value)

tenta.print_results()

tenta.write_to_json_file('exam.json')

tenta2 = read_from_json_file('exam.json')

tenta2.print_results()