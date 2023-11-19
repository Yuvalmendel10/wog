import random
import time
import os

def generate_sequence(difficulty):
    numbers = []
    for i in range(int(difficulty)):
        numbers.append(random.randint(1,101))
    print(' '.join(map(lambda number: str(number), numbers)), end='')
    time.sleep(1)
    print('\r ')
    os.system('cls')

    return numbers

def get_list_from_user(difficulty):
    numbers = []
    words = {0: 'first', 1: "second", 2: "third", 3: "forth", 4: "fifth"}
    for i in range(int(difficulty)):
        numbers.append(int(input(f"insert the {words[i]} number that you have seen and press enter: ")))
    return numbers

def is_list_equal(difficulty):
    generated_list = generate_sequence(difficulty)
    player_list = get_list_from_user(difficulty)

    if sorted(generated_list) == sorted(player_list):
        return True
    else:
        return False

def play(difficulty):
    if is_list_equal(difficulty):
        return True
    else:
        return False

