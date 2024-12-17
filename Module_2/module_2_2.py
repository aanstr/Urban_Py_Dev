first = input('Введите 1 число: ')
second = input('Введите 2 число: ')
third = input('Введите 3 число: ')
if first==second==third:
    print(3)
elif first==second or second==third or first==third:
    print(2)
else: print(0)
