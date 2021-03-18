import numpy as np

def game_core(secret_num):
    """Метод половинного деления - приближаемся к результату, используя на каждом шаге середину диапазона"""

    lo_bound = 0    # нижняя граница диапазона поиска
    hi_bound = 101  # верхняя граница диапазона поиска

    if secret_num<=lo_bound or secret_num>=hi_bound:    # проверить на соблюдение правил игры
        return -1   # нарушение правил игры - загаданное число вне диапазона
    else:
        count = 0  # инициализировать счетчик попыток

    while True:
        count += 1  # +1 счетчик попыток
        guess_num = lo_bound + int((hi_bound-lo_bound)/2)    # попытаться угадать
        if guess_num<secret_num:  # искомое число больше догадки
            lo_bound = guess_num    # подтянуть нижнюю границу
        elif guess_num>secret_num:    # искомое число меньше догадки
            hi_bound = guess_num    # опустить верхнюю границу
        else:   # ура - нашли!
            break

    return count    # вернуть счетчик попыток


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    np.random.seed(1)   # инициализация ПСЧ
    serie_num = 1000    # кол-во экспериментов
    lo_bound = 1    # диапазон для генерации случайных чисел
    hi_bound = 101  # для получения нарушений установить hi_bound > 101

    random_array = np.random.randint(lo_bound, hi_bound, size=serie_num)   # построить список загаданных чисел
    count_ls = list(map(game_core, random_array))   # выполнить серию угадываний
    valid_ls = list(filter(lambda x: x>0, count_ls))    # отбросить нарушения правил
    score = int(np.mean(valid_ls))  # расчет среднего кол-ва попыток

    print("Загадано чисел:", len(random_array))
    print("Получено результатов:", len(count_ls))
    print("Из них валидные:", len(valid_ls))
    print("Нарушения правил:", len(count_ls) - len(valid_ls))
    print("------------------------------")
    print("Среднее число попыток:", score)
    return score


score_game(game_core)
