import os

SCORES_FILE_NAME = 'scores.txt'
BAD_RETURN_CODE = 401

def Screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n' * 100)