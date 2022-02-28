from task_2 import password_generator
from task_3 import safety_check


def safe_pass_generator() -> str:
    res_password = ''
    counter = 0
    while not safety_check(res_password):
        counter += 1
        res_password = password_generator()
    return f"Ваш пароль {res_password} (пароль был получен с попытки номер {counter})"


print(safe_pass_generator())
