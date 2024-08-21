numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in numbers[1:]:
    for j in numbers[1:i-1]:
        if i % j == 0:
            is_prime = False
            break
        else:
            is_prime = True
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
print(f'Primes: {primes}')
print(f'Not Primes: {not_primes}')
