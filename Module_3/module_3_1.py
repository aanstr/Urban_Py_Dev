calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    len_ = len(string)
    tuple_ = len_, string
    return tuple_


def is_contains(string, list_to_search):
    count_calls()
    print(1)



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
