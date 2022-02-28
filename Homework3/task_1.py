from random import randint

idea = 1000
number = randint(1, 10)
# print(number)
while not idea == number:
    idea = int(input("Пропробуйте угадать число. Введите целое число от 1 до 10 "))
    if idea == number:
        print("Вы угадали!")
    else:
        print("Вы не угадали... Попробуйте еще раз")

idea = 1000
number = randint(1, 10)
# print(number)
while not idea == number:
    idea = int(input("Пропробуйте угадать число. Введите целое число от 1 до 10 "))
    if idea > number:
        print("Ваше предположение больше загаданного числа. Попробуйте еще раз")
    elif idea < number:
        print("Ваше предположение меньше загаданного числа. Попробуйте еще раз")
    else:
        print("Вы угадали!")
