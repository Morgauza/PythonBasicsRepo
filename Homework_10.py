def linear_search(numbers, target):
    """Линейный поиск числа в списке"""
    for i, num in enumerate(numbers):
        if num == target:
            return i
    return None


def binary_search(numbers, target):
    """Бинарный поиск числа в списке"""

    sorted_numbers = sorted(numbers)

    left, right = 0, len(sorted_numbers) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_numbers[mid] == target:
            return mid
        elif sorted_numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None


def bubble_sort(numbers):
    """Сортировка списка пузырьком"""
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


def get_min(numbers):
    """Находит минимальное значение в списке"""
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val


def get_max(numbers):
    """Находит максимальное значение в списке"""
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val


def get_avg(numbers):
    """Вычисляет среднее арифметическое списка"""
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


def get_median(numbers):
    """Находит медианное значение в списке"""
    # создаём пустой словарь, если тот же ключ(наши числа) попадается ещё раз, то увеличиваем его значение на 1.
    #  Это работает из-за того что не может быть одинаковых ключей
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # проходимcя по значениям созданного словаря, находим максимальную частоту
    max_frequency = 0
    for val in frequency.values():
        if val > max_frequency:
            max_frequency = val

    # находим предполагаемое медианное число. Если их несколько, потом в main возвращаем среднее по списку, иначе
    # медианное число найдено
    frequently_encountered = []
    for key, val in frequency.items():
        if val == max_frequency:
            frequently_encountered.append(key)

    if len(frequently_encountered) > 1:
        return None

    return frequently_encountered[0]

def print_menu():
    """Выводит меню программы"""
    print("МЕНЮ ПРОГРАММЫ:")
    print("1. Найти число (линейный поиск)")
    print("2. Найти число (бинарный поиск)")
    print("3. Отсортировать список пузырьком")
    print("4. Найти минимальное значение")
    print("5. Найти максимальное значение")
    print("6. Найти среднее арифметическое")
    print("7. Найти медиану")
    print("8. Выйти")



def main():
    """Основная функция программы"""

    numbers_input = input("Введите список чисел через пробел: ")
    numbers = [float(x) for x in numbers_input.split()]
    print(f"Ваш список: {numbers}")

    # Проверка на пустой список
    if len(numbers) == 0:
        print("Список пуст!")
        return

    while True:
        print_menu()
        choice = input("Выберите опцию (1-8): ")

        if choice == '1':
            # Линейный поиск
            target = float(input("Введите число для поиска: "))
            index = linear_search(numbers, target)
            if index is not None:
                print(f"Число {target} найдено на позиции {index}")
            else:
                print(f"Число {target} не найдено в списке")

        elif choice == '2':
            # Бинарный поиск
            target = float(input("Введите число для поиска: "))
            found = binary_search(numbers, target)
            if found is not None:
                print(f"Число {target} найдено в отсортированном списке на позиции {found}")
            else:
                print(f"Число {target} не найдено в списке")

        elif choice == '3':
            # Сортировка пузырьком
            original_numbers = numbers.copy()
            sorted_numbers = bubble_sort(numbers)
            numbers = sorted_numbers
            print(f"Исходный список: {original_numbers}")
            print(f"Отсортированный список: {sorted_numbers}")

        elif choice == '4':
            # Минимальное значение
            min_val = get_min(numbers)
            print(f"Минимальное значение: {min_val}")

        elif choice == '5':
            # Максимальное значение
            max_val = get_max(numbers)
            print(f"Максимальное значение: {max_val}")

        elif choice == '6':
            # Среднее арифметическое
            avg_val = get_avg(numbers)
            print(f"Среднее арифметическое: {avg_val:.2f}")

        elif choice == '7':
            # Медиана
            median_val = get_median(numbers)
            if median_val is not None:
                print(f"Медианное значение: {median_val:.2f}")
            else:
                print(f"Медианного значения нет, среднее по списку: {sum(numbers)/len(numbers)}")


        elif choice == '8':
            # Выход
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


# Запуск программы
if __name__ == "__main__":
    main()