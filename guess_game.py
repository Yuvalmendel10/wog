import random

def generate_number(difficulty):
    secret_number = random.randint(1, int(difficulty))
    return secret_number


def get_guess_from_user(difficulty):
    while True:
        selected_number = input(f"enter a number between 1 to {difficulty}: ")
        if 1<=int(selected_number)<=3:
            return selected_number
        else:
            print("you need to select a number between 1 - 3, lets try and select it again: ")

def compare_results(difficulty):
    if int(generate_number(difficulty)) == int(get_guess_from_user(difficulty)):
        return True
    else:
        return False

def play(difficulty):
    if compare_results(difficulty):
        return True
    else:
        return False

