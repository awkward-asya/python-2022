from random import randint


def password_generator() -> str:
    pass_digits = []
    pass_len = randint(7, 10)
    while len(pass_digits) != pass_len:
        pass_digits.append(chr(randint(33, 126)))
    password = ''.join(map(str, pass_digits))
    return password


# print(password_generator())
