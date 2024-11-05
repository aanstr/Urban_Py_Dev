import multiprocessing as mp
from time import time

filenames = [f'./file {number}.txt' for number in range(1, 5)]


def read_info(name):
    all_data = []
    with open(name) as __file:
        for line in __file.readlines():
            all_data.append(line)


if __name__ == '__main__':
    time_start = time()
    for file in filenames:
        read_info(file)
    time_end = time() - time_start
    print(f'Время линейного выполнения {time_end:.3f} сек')

    time_start = time()
    with mp.Pool(4) as pool:
        pool.map(read_info, filenames)
    time_end = time() - time_start
    print(f'Время многопроцессного выполнения {time_end:.3f} сек')
