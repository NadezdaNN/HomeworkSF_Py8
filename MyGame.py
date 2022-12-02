"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""

import numpy as np
"""number = np.random.randint(1,101)
count = 0

while True:
    count +=1
    predict_number = int(input("Guess the numbet from 1 to 100"))

    if predict_number > number:
        print('The number mast be less!')
    elif predict_number < number:
        print('The number mast be greater!')
    else:
        print(f'You guessed the number! This number = {number}, for {count} attempts')
        break"""

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 
    predict_number = np.random.randint(1,101)
    tmp1=1
    tmp2=100

    while True:
        count += 1
        
        if predict_number < number:
            tmp1=predict_number
            predict_number = round((predict_number+tmp2)/2)

        elif predict_number > number:
            tmp2=predict_number
            predict_number = int((predict_number+tmp1)/2)
            
        else:# number == predict_number:
            #print(count)
            break
        
    return count

#print(f'Number of attempts: {random_predict()}')

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: функция угадывания
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size = 1000)
    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

score_game(random_predict)


# xnj,s dytcnb bpvtytybz
