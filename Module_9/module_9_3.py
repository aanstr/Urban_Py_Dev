first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(i) - len(j) for i, j in zip(first, second) if len(i) != len(j))
second_result = (len(i) == len(j) for i, j in zip(first, second))

print(list(first_result))
print(list(second_result))
