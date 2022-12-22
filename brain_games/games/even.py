from random import randint


main_question = 'Answer "yes" if the number is even, otherwise answer "no".'


def run():
    random_num = randint(0, 100)
    if random_num % 2 == 0:
        return random_num, "yes"
    else:
        return random_num, "no"
