def is_prime(func):
    def wrapper(*args, **kwargs):
        __result = func(*args, **kwargs)
        for i in range(2, int(__result ** 0.5) + 1):
            if __result % i != 0:
                print('Простое')
                break
            else:
                print('Составное')
                break
        return __result

    return wrapper


@is_prime
def sum_three(*args):
    __result = 0
    for num in args:
        __result += num
    return __result


result = sum_three(2, 3, 6)
print(result)
