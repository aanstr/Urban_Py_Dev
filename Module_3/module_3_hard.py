sum_ = 0


def calculate_structure_sum(args):
    global sum_
    result_ = 0
    array_ = args
    for i in array_:
        result_ = 0
        print(i)
        print(f'Result {sum_}')
        if isinstance(i, int) or isinstance(i, float):
            result_ += i
        elif isinstance(i, str):
            result_ += len(i)
        elif isinstance(i, list):
            result_ += calculate_structure_sum(i)
        elif isinstance(i, tuple):
            result_ += calculate_structure_sum(i)
        elif isinstance(i, set):
            result_ += calculate_structure_sum(i)
        elif isinstance(i, dict):
            for j in i:
                print(j)
                i.get(j)
                result_ += calculate_structure_sum(j)
    #          str(i.values())
    #          str(i.values())
    #      result_ += calculate_structure_sum(i)
        print(f'Result_ {result_}')
    sum_ += result_
    return sum_


# 1+2+3+ len('a') +4+ len('b') +5+6+ len('cube') +7+ len('drum') +8+ len('Hello') +2+ len('Urban') + len('Urban2')+35=99

data_structure = [
    [1, 2, 3],  # 6
    {'a': 4, 'b': 5},  # 17
    (6,  # 23
     {'cube': 7, 'drum': 8}  # 46
     ),
    "Hello",  # 51
    ((), [{(2,  # 53
            'Urban',  # 58
            ('Urban2', 35)  # 64, 99
            )}])
]
#  print(list(data_structure[1]))
result = calculate_structure_sum(data_structure)
print(result)
