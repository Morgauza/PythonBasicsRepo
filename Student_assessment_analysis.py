number_of_students = int(input("Количество студентов: "))
students = []
for i in range(number_of_students):
    name = input("Имя студента: ")
    marks = [int(x) for x in input("Введите оценки студента через пробел: ").split()]
    students.append([name, marks])

averages = []
for student in students:
    name, marks = student
    total = 0
    count = 0
    for num in marks:
        total += num
        count += 1
    average = total / count
    averages.append(average)

print("\nИмя        Средний балл")
for i in range(len(students)):
    name = students[i][0]
    avg = averages[i]
    print(f"{name:<10} {avg}")


excellent_students = [students[i][0] for i in range(len(students)) if averages[i] >= 4.5]
if excellent_students:
    print(f"\nТе у кого средний балл больше 4.5: {', '.join(excellent_students)}")
else:
    print()

max_avg = averages[0]
min_avg = averages[0]
best_student = students[0][0]
worst_student = students[0][0]

for i in range(1, len(averages)):
    if averages[i] > max_avg:
        max_avg = averages[i]
        best_student = students[i][0]
    if averages[i] < min_avg:
        min_avg = averages[i]
        worst_student = students[i][0]

print(f"\nЛучший студент: {best_student} ({max_avg})")
print(f"Худший студент: {worst_student} ({min_avg})")

group_total = 0
for avg in averages:
    group_total += avg
group_avg = group_total / len(averages)
print(f"Средний балл по группе: {group_avg}")