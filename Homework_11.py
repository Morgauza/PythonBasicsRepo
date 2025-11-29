import math

def solve_quadratic(a, b, c):
    D = b**2 - 4 * a * c

    if D < 0:
        return "Нет действительных корней"
    elif D == 0:
        x = -b / (2 * a)
        return f"Один корень: {x}"
    else:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return f"Два корня: {x2} и {x1}"
#     x2 будет всегда меньше x1 из-за минус math.sqrt(D)

# a = float(input("Введите параметр a: "))
# b = float(input("Введите параметр b: "))
# c = float(input("Введите параметр c: "))

# print(solve_quadratic(a, b, c))


def make_report(title, **sections):
    print(f"==={title}===")
    total = 0
    for key, value in sections.items():
        print(f"{key}: {value}")
        total += value
    print(f"общая сумма: {total}")


name = "Отчёт:Продажи"
book = {"north":12000, "south":8500, "west":9000, "east":8700}

make_report(name, **book)











