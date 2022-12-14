''' Created by Victor Pinheiro - random functions to play lotto'''
import random


#  lotto regular
def lotto_no_skipp(seed=0, game=12):
    '''consider the default of 12 games and if seed is 0 it will be fully python random'''
    if seed == 0:
        random.seed()
    else:
        random.seed(seed)
    for i in range(game):
        numbers = []
        for j in range(1000):
            number = random.randint(1, 45)
            if number not in numbers:
                numbers.append(number)
            if len(numbers) == 6:
                break

        print(numbers)



# Lotto skipp
def lotto_skipp(seed=0, jump=0, game=12):
    if seed == 0:
        random.seed()
    else:
        random.seed(seed)

    for i in range(game):
        numbers = []
        for j in range(1000):
            for i in range(jump):
                continue
            number = random.randint(1, 45)
            if number not in numbers:
                numbers.append(number)
            if len(numbers) == 6:
                break

        print(numbers)

# power ball
def powerball_powerhit(seed=0, jump=0, game=2):
    if seed == 0:
        random.seed()
    else:
        random.seed(seed)

    for i in range(game):
        numbers = []
        for j in range(1000):
            for i in range(jump):
                continue
            number = random.randint(1, 35)
            if number not in numbers:
                numbers.append(number)
            if len(numbers) == 7:
                break

        print(numbers)
