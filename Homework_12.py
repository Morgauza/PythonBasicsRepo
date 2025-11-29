students = [ {"name": "Анна", "score": 88}, {"name": "Павел", "score": 95},
             {"name": "Игорь", "score": 72}, {"name": "Марина", "score": 91}, ]

def study(students):
    students = sorted(students, key=lambda student: student["score"], reverse=True)
    students = list(filter(lambda x: x["score"] > 85, students))
    students = list(map(lambda x: x['name'].upper(), students))
    print(students)

study(students)















