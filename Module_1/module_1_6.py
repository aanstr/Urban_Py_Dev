my_dict = {'Pasha': 1984, 'Sasha': 2001, 'Katya': 1993, 'Masha': 2015}
print(my_dict)
print(my_dict.get('Katya'))
print(my_dict.get('Oleg'))
my_dict.update({'Maksim': 2008, 'Anton': 1991})
print(my_dict.pop('Sasha'))
print(my_dict)
my_set = {1, 2, 5, 3, 1, 8, 2, 3, 6, 5, 1}
print(my_set)
my_set.add('Attr')
my_set.add((1, 2, 3))
my_set.discard(1)
print(my_set)
