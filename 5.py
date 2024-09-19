def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])

    if len(str_number) > 1:
        multiplier = get_multiplied_digits(int(str_number[1:]))
        if multiplier:
            return first * get_multiplied_digits(int(str_number[1:]))

    return first


result = get_multiplied_digits(40203)
print(result)

print('Дополнительные тесты:')
print(get_multiplied_digits(4020))
print(get_multiplied_digits(0))
print(get_multiplied_digits(1))
print(get_multiplied_digits(1111))
