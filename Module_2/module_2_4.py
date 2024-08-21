numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = False
for i in numbers[1:]:
    for j in numbers[1:i]:
        if i > j and i % j == 0:
            is_prime = False
            break
        elif i % j == 0:
            is_prime = True
        else:
            continue
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
print(f'Primes: {primes}')
print(f'Not Primes: {not_primes}')
