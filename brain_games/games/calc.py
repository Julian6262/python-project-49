from random import randint, choice


main_question = 'What is the result of the expression?'


def run():
    num1 = randint(0, 30)
    num2 = randint(0, 30)
    operator = choice(['+', '-', '*'])
    if operator == '+':
        return f'{num1} + {num2}', str(num1 + num2)
    if operator == '-':
        return f'{num1} - {num2}', str(num1 - num2)
    if operator == '*':
        return f'{num1} * {num2}', str(num1 * num2)
