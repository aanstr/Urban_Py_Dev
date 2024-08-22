n = int(input('Введите число (3-20): '))


def result(n):
    get_result = []
    for i in range(1, n):
        pairs = []
        for j in range(1, 20):
            k = i + j
            if i < j and n % k == 0:
                pairs.append(i)
                pairs.append(j)
        get_result.append(pairs)
    get_result = sorted(get_result)
    return get_result


print('Пароль: ', *result(n))
