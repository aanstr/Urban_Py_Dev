sum_ = 0


def calculate_structure_sum(args):
    global sum_
    for i in args:
        if isinstance(i, int) or isinstance(i, float):
            sum_ += i
        elif isinstance(i, str):
            sum_ += len(i)
        elif isinstance(i, dict):
            for j in i:
                sum_ += (i.get(j))
                sum_ += len(j)
        else:
            calculate_structure_sum(i)
    return sum_


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(f'сумма: {result}')
