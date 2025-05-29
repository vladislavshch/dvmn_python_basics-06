PASSWORD = input("Введите пароль: ")


def is_very_long(PASSWORD):
    if len(PASSWORD) < 12:
        return False
    return True


def has_digit(PASSWORD):
    return any(letter.isdigit() for letter in PASSWORD)


def has_upper_letters(PASSWORD):
    return any(letter.isupper() for letter in PASSWORD)


def has_lower_letters(PASSWORD):
    return any(letter.islower() for letter in PASSWORD)


def has_symbols(PASSWORD):
    return any(not letter.isalpha() and not letter.isdigit() for letter in PASSWORD)


def main():
    score = 0
    checks = [
        is_very_long(PASSWORD),
        has_digit(PASSWORD),
        has_lower_letters(PASSWORD),
        has_upper_letters(PASSWORD),
        has_symbols(PASSWORD),
    ]
    for check in checks:
        if check:
            score += 2
    print("Рейтинг пароля: " + str(score))


if __name__ == '__main__':
    main()