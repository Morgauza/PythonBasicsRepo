a = int(input("Введите первое число "))
b = int(input("Введите второе число "))


max_sum = 0
our_num = a

for num in range(a, b+1):
    first_sum = 0
    i = 1
    while i <= num:
        if num % i == 0:
            first_sum += i
        i += 1
    if first_sum > max_sum:
        max_sum = first_sum
        our_num = num
    elif first_sum == max_sum and num > our_num:
        our_num = num
print(f"Число с максимальной суммой делителей {our_num},сумма делителей этого числа {max_sum}")





