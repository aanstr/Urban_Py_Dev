import random

rand_nums = [random.randint(1, 100) for _ in range(10)]


def summ(numbers):
    result = 0
    for num in numbers:
        # print(num)
        result += int(num)
    return result


print(summ(rand_nums))


import numpy as np

rand_arr = np.random.randint(1, 100, 20)
print(rand_arr)
print(np.average(rand_arr))

import pandas as pd


file = '/content/wiki.csv'
df = pd.read_csv(file, encoding='cp1251')
print(df.head())

import matplotlib.pyplot as plt

plt.plot(df['Год'], df['Москва'] / 1000000, label='Москва')
plt.plot(df['Год'], df['Санкт-Петербург'] / 1000000, label='Санкт-Петербург')
plt.xlabel('Год')
plt.ylabel('Население, млн')
plt.title('Динамика изменения населения городов')
plt.legend()
plt.show()
