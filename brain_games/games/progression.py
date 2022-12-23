from random import randint


main_question = 'What number is missing in the progression?'


def run():
    first_num = randint(1, 30)  # set the first value (1 to 30)
    progression_len = first_num * (randint(5, 10) + 1)  # set length (5 to 10)
    progression = list(range(first_num, progression_len, first_num))
    secret_index = randint(0, len(progression) - 1)
    correct_answer = progression[secret_index]
    progression[secret_index] = '..'
    progression = list(map(str, progression))
    progression = ' '.join(progression)
    return progression, str(correct_answer)
