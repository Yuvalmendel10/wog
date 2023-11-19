from currency_converter import CurrencyConverter
import random

def get_money_interval(difficulty, dollars_for_guessing):
    c = CurrencyConverter()
    conversion = c.convert(dollars_for_guessing, 'USD', 'ILS')
    difficulty = int(difficulty)
    if difficulty == 1:
        return [conversion-50, conversion+50]
    elif difficulty == 2:
        return [conversion-40, conversion+40]
    elif difficulty == 3:
        return [conversion-30, conversion+30]
    elif difficulty == 4:
        return [conversion-20, conversion+20]
    else:
        print("n")
        return [conversion-10, conversion+10]


def get_guess_from_user(dollars_for_guessing):
    return input(f"insert your calculation - how much is {dollars_for_guessing} dollars in israeli shekels? ")


def is_list_equal(difficulty):
    dollars_for_guessing = random.randint(1, 1000)
    real_calculation = get_money_interval(difficulty, dollars_for_guessing)
    user_guessing = get_guess_from_user(dollars_for_guessing)
    print(real_calculation[0],int(user_guessing),real_calculation[1])
    if real_calculation[0] <= int(user_guessing) <= real_calculation[1]:
        return True
    else:
        return False

def play(difficulty):
    if is_list_equal(difficulty):
        return True
    else:
        return False




