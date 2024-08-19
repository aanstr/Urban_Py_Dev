immutable_var = (1, 2, 'a', 'b')
print(immutable_var)
# immutable_var[0] = 2
# Значение элемента кортежа не удается изменить, т.к. кортеж - неизменяемый объект, хотя может содержать изменяемые элементы
# print(immutable_var)
mutable_list = [1, 2, 'a', 'b', 3]
print(mutable_list)
mutable_list[4] = 'redacted'
print(mutable_list)
