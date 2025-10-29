import random

choices = ['камень', 'ножницы', 'бумага']

print("Выберите: камень, ножницы или бумага")

user_choice = input("Ваш выбор: ").lower()
computer_choice = random.choice(choices)

print(f"Компьютер выбрал: {computer_choice}")

if user_choice not in choices:
    print("Ошибка! Выберите камень, ножницы или бумага")
else:
    if user_choice == computer_choice:
        print("Ничья!")
    elif (user_choice == 'камень' and computer_choice == 'ножницы') or \
         (user_choice == 'ножницы' and computer_choice == 'бумага') or \
         (user_choice == 'бумага' and computer_choice == 'камень'):
        print("Вы выиграли!")
    else:
        print("Вы проиграли!")
