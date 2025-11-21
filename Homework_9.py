import math

def distance(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> float:
    """
    Вычисляет расстояние между двумя точками в трёхмерном пространстве.
    """
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) + math.pow(z2 - z1, 2))

first_point = [float(num) for num in input("Введите координаты первой точки(x y z) ").split()]
second_point = [float(num) for num in input("Введите координаты второй точки(x y z) ").split()]

# распоковка
x1, y1, z1 = first_point
x2, y2, z2 = second_point

print(f"Расстояние между точками  равно {distance(x1, y1, z1, x2, y2, z2):.2f}")

