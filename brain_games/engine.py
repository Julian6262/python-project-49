from brain_games.engine_code.greet import welcome_user
from brain_games.engine_code.even import even
from prompt import string


def start():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    number_of_rounds = 3
    for _ in range(number_of_rounds):
        question, correct_answer = even()
        print(f"Question: {question}")
        answer = string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'."
                  f"\nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
