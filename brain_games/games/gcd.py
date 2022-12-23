from random import randint


main_question = 'Find the greatest common divisor of given numbers.'


def run():
    num1 = randint(0, 30)
    num2 = randint(0, 30)
    correct_answer = gcd(num1, num2)
    return f'{num1} {num2}', str(correct_answer)


def gcd(num1, num2):
    if(num2 == 0):
        return num1
    else: 
        return gcd(num2, num1 % num2) 
