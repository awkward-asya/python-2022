# задание 2.1

students = ["Вася", "Маша", "Петя", "Дима", "Марина", "Люба", "Коля", "Ваня"]
grades = {"Вася" : 4, "Петя" : 9, "Марина" : 8, "Люба" : 4, "Коля" : 5, "Ваня": 10}
for item in students:
    if item not in grades:
        print(f'{item} контрольную работу не писал(а)')
    else:
        print(f'Имя студента: {item}, оценка: {grades[item]}')

# задание 2.2
print('Отличные оценки получили:')
for item in grades:
    if grades[item] >= 8:
        print(item)

# задание 2.3
good = []
bad = []
for item in grades:
    if grades[item] >= 5:
        good.append(item)
    else:
        bad.append(item)
        
