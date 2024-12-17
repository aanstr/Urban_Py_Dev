def custom_write(file_name, strings):
    with open(file_name, 'w', encoding='utf-8') as file:
        strings_positions = {}
        num_ = 1
        for str_ in strings:
            tuple_ = (num_, file.tell())
            file.write(f'{str_}\n')
            num_ += 1
            strings_positions.update({tuple_: str_})
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
