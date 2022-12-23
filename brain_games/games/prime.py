from random import randint


main_question = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def run():
    number = randint(0, 100)
    if number < 2:
        return number, 'no'
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return number, 'no'
    return number, 'yes'
