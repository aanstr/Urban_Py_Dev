def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    while len(str_number) > 1:
        result_inner = first * get_multiplied_digits(int(str_number[1:]))
        if result_inner > 0:
            return result_inner
        else:
            return first
    else:
        return first


result = get_multiplied_digits(40203)
print(result)
result = get_multiplied_digits(1000)
print(result)
result = get_multiplied_digits(250001)
print(result)