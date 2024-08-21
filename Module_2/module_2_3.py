my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
count = 0
while count < len(my_list):
    num = my_list[count]
    count = count + 1
    if num > 0:
        print(num)
    elif num == 0:
        continue
    else:
        break
