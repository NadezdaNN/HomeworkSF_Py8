"""The program guess the number made by a computer 
in the minimum count of attempts
"""

import numpy as np


def random_predict(number:int=1) -> int:
    """Guessing the number

    Args:
        number (int, optional): the number made by a computer. Defaults to 1.

    Returns:
        int: number of attempts
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
            
        else:            
            break

        if count > 20:
            break
        
    return count


def score_game(random_predict) -> int:
    """For how many attempts on average out of 1000 approaches 
    does our algorithm guess

    Args:
        random_predict (_type_): guessing function

    Returns:
        int: average number of attempts
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size = 1000)
    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f'This algorithm guesses the number on average for: {score} attempts')
    return score


if __name__ == "__main__":    
    score_game(random_predict)