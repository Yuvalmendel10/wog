from utils import SCORES_FILE_NAME
from os import path


def add_score(difficulty):
    current_score = load_score()
    current_score += (difficulty * 3) + 5
    with open(SCORES_FILE_NAME, 'w') as file:
        file.write(str(current_score))

def load_score():
    if path.exists(SCORES_FILE_NAME):
        with open(SCORES_FILE_NAME, 'r') as file:
            current_score = file.read()
            if current_score.isdigit():
                current_score = int(current_score)
            else:
                current_score = 0
    else:
        current_score = 0
    return current_score



