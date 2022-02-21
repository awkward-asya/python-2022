print('Введите Ваше имя: ')
name = input().lower()
if len(name) < 5:
    print('Введите Вашу фамилию: ')
    surname = input().upper()
    name = name.upper()
    print(name + surname)
else:
    print(name)
