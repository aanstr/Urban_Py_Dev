team1_num = 5
team2_num = 6
score_1 = 44
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1 + score_2
time_avg = team1_time + team2_time / 2
# challenge_result = 'Победа команды Волшебники данных!'
msg = []


def challenge_result():
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        result = 'Победа команды Мастера кода!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        result = 'Победа команды Волшебники Данных!'
    else:
        result = 'Ничья!'
    return result


# Использование %:
msg.append("В команде Мастера кода участников: %s !" % team1_num)
msg.append("Итого сегодня в командах участников: %s и %s !" % (5, 6))

# Использование format():

msg.append("Команда Волшебники данных решила задач: {} !".format(score_2))
msg.append(" Волшебники данных решили задачи за {} с !".format(team1_time))

# Использование f-строк:

msg.append(f'Команды решили {score_1} и {score_2} задач.')
msg.append(f'Результат битвы: {challenge_result()}')
msg.append(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')

for i in msg:
    print(i)
