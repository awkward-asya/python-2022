def safety_check(password: str) -> bool:
    if (len(password) >= 8 and
            any(char.isdigit() for char in password) and
            any(char.islower() for char in password) and
            any(char.isupper() for char in password)):
        return True
    else:
        return False


# print(safety_check("123aA"))
# print(safety_check("1aaaB78"))
# print(safety_check("12aaaB78"))
