sum_ = 0


def calculate_structure_sum(args):
    global count
    global sum_
    for i in args:
        result_ = 0
        if isinstance(i, int) or isinstance(i, float):
            result_ += i
        elif isinstance(i, str):
            result_ += len(i)
        elif isinstance(i, dict):
            for j in i:
                result_ += (i.get(j))
                result_ += len(j)
        else:
            calculate_structure_sum(i)
        sum_ += result_
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
