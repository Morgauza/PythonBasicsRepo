# zadacha 1
# a = int(input("Введите a: "))
# b = int(input("Введите b: "))
# if a > b:
#     print("a больше b")
# elif a < b:
#     print("a меньше b")
# else:
#     print("a равно b")

# zadacha2
# nums = [int(num) for num in input("ВВедите целые числа через пробел ").split()]
# sum1 = 0
# sum2 = 0
# for n in nums:
#     if n % 2 == 0:
#         sum1 += n
#     else:
#         sum2 += n
# print(f"сумма чётных {sum1}")
# print((f"сумма нечётных {sum2}"))

# 3zadacha
# numbers = [5, 3, 8, 6, 2, 8, 3]
# unique_nums = sorted(set(numbers), reverse=True)
#
# if len(unique_nums) >= 2:
#     print("Второе по величине число:", unique_nums[1])
# else:
#     print("Нет второго по величине числа")

# task4
# n = int(input())
# nums = list(range(1, n+1))
# correct_nums = []
# for i in nums:
#     if i % 3 == 0 or i % 5 == 0:
#         continue
#     correct_nums.append(i)
# print(correct_nums)

# task5
# numbers = [5, 3, 8, 6, 2, 8, 3]
# max_num = numbers[0]
# for n in numbers:
#     if n > max_num:
#         max_num = n
# print("Максимум:", max_num)

# task6
# nums =[float(x) for x in input("Введите 5 чисел через пробел ").split()]
# sum = 0
# for num in nums:
#     sum += num
# print(sum)

# task7
# Names =  ["Анна", "Борис", "Катя", "Дима"]
# for name in Names:
#     if name.startswith("К"):
#         print(name)

# task8
# n = int(input())
# correct_nums = []
# for i in range(1, n+1):
#     if i % 3 == 0:
#         continue
#     correct_nums.append(i)
# print(correct_nums)

# task9
# n = int(input("Введите n: "))
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print("Факториал:", fact)

# task10
# nums = [int(x) for x in input().split()]
# correct_nums = []
# for num in nums:
#     if num > sum(nums) / len(nums):
#         correct_nums.append(num)
# print(correct_nums)

# task11
# words = ["apple", "banana", "cherry", "date"]
# upp_words = [word.upper() for word in words]
# print(upp_words)

# task12
# n = int(input())
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print(f"{i}*{j}={i*j}", end="\t")
# print()

# task13
# nums = [int(x) for x in input().split()]
# a = 0
# for i in range(1, len(nums)):
#     if nums[i] > nums[i-1]:
#         a += 1
# print(a)

# task14
# nums = [5, 2, 3, 2, 5, 2]
# while 2 in nums:
#     nums.remove(2)
# print(nums)

# task15

# words = input().split()
# max_word = max(words, key=len)
# print(max_word)




























