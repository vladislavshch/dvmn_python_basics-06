

def is_very_long(password):
    return len(password) > 12


def has_digit(password):
    return any(letter.isdigit() for letter in password)


def has_upper_letters(password):
    return any(letter.isupper() for letter in password)


def has_lower_letters(password):
    return any(letter.islower() for letter in password)


def has_symbols(password):
    return any(not letter.isalpha() and not letter.isdigit() for letter in password)


def main():
    password = input("Введите пароль: ")
    score = 0
    checks = [
        is_very_long(password),
        has_digit(password),
        has_lower_letters(password),
        has_upper_letters(password),
        has_symbols(password),
    ]
    for check in checks:
        if check:
            score += 2
    print("Рейтинг пароля: " + str(score))


if __name__ == '__main__':
    main()