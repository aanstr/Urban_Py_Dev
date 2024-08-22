n = int(input('Введите число (3-20): '))


def result(n):
    get_result = ''
    for i in range(1, n):
        pairs = ''
        for j in range(1, 20):
            k = i + j
            if i < j and n % k == 0:
                pairs += str(i) + str(j)
        get_result += pairs
    get_result = get_result
    return get_result


print('Пароль: ',result(n))
