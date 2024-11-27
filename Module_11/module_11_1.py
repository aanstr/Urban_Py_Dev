import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def file_import(filename, encoding='cp1251'):
    df = pd.read_csv(filename, encoding=encoding)
    return df

def arr_(df):
    arr = np.array([df['Москва'], df['Санкт-Петербург']])
    print(arr)
    print(f'Размерность массива: {arr.ndim}')
    print(f'Строк, столбцов: {arr.shape}')
    print(f'Элементов: {arr.size}')


def plot(df):
    plt.plot(df['Год'], df['Москва'] / 1000000, label='Москва')
    plt.plot(df['Год'], df['Санкт-Петербург'] / 1000000, label='Санкт-Петербург')
    plt.xlabel('Год')
    plt.ylabel('Население, млн')
    plt.title('Динамика изменения населения городов')
    plt.legend()
    plt.show()


def main():
    filename = 'wiki.csv'
    file = file_import(filename)
    arr_(file)
    print(file)
    plot(file)


if __name__ == '__main__':
    main()
