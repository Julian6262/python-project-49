from random import randint


main_question = 'Answer "yes" if the number is even, otherwise answer "no".'


def even():
    question = randint(0, 100)
    if (question % 2 == 0):
        return question, "yes"
    if question % 2 != 0:
        return question, "no"