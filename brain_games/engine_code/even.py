from random import randint


def even():
    question = randint(0, 100)
    if (question % 2 == 0):
        return question, "yes"
    if question % 2 != 0:
        return question, "no"
