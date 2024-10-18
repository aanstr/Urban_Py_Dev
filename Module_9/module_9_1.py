def apply_all_func(int_list, *functions):
    for i in int_list:
        try:
            if not isinstance(i, int or float):
                raise TypeError
        except TypeError:
            print(f'Следует передать список чисел\n(Передано: {int_list})')
    try:
        return {func.__name__: func(int_list) for func in functions}
    except TypeError:
        print("Ошибка данных на входе")


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
print(apply_all_func([6, 'test', 15, 9], max, min))
