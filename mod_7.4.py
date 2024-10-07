team1 = 'Команда Мастера кода'
team2 = 'Команда  Волшебники данных'

def num(team1_num = 0, team2_num = 0):
    print('В команде Мастера кода участников: %s' % (team1_num))
    print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))


    score_1 = 0
    score_2 = 0

def time(team1_time=0, team2_time=0, tasks_total=0):
    time1 = team1_time
    time2 = team2_time
    print('Команда {} решила задач: {}!'.format(team2, score_2))
    print('{} решили задачи за {} cек. !'.format(team2, time2))

def challenge_result(tasks_total = 0, time_avg = 0):
    print(f'Команды решили {score_1} и {score_2} задач.')
    if score_1 > score_2:
        print(f'Результат битвы: победа команды {team1} !')
    else:
        print(f'Результат битвы: победа команды {team2} !')

    print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу')


# score_1 = 42
# score_2 = 42
# team1_time = 60
# team2_time = 65
# tasks_total = 82
# time_avg = 82
num(team1_num=5, team2_num=6)
score_1 = 40
score_2 = 42
time(team1_time=1552.512, team2_time=2153.31451)
challenge_result(tasks_total=82, time_avg = 45.2)

