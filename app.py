
import guess_game
import currency_roulette_game
import memory_game
from score import add_score

def welcome():
    name = input("Enter your name: ")
    print(f"Hi {name} and welcome to the World of Games: The Epic Journey")

def start_play():
    games = ["Memory Game", "Guess Game", "Currency Roulette"]

    def select_game():
        return input("Select which game do you want to play:\n"
                            "for \"Memory Game\" press 1 \n"
                            "for \"Guess Game\" press 2 \n"
                            "for \"Currency Roulette\" press 3 \n"
                                "(than press enter): ")

    while True:
        game_number = select_game()
        if game_number.isdigit() and 1 <= int(game_number) <= 3:
            break
        else:
            print("you need to select a number between 1 - 3, lets try and select it again")

    while True:
        difficulty_level = input("Now select the difficulty level of the game from 1-5 (1 is the easiest) (and than press enter): ")
        if difficulty_level.isdigit() and 1 <= int(difficulty_level)<=5:
            break
        else:
            print("the difficulty level you selected is not in range of 1 to 5. try again")

    game = games[int(game_number) - 1]
    print(f"you selected the game: \"{game}\" on difficulty {difficulty_level}")

    if game == 'Memory Game':
        result = memory_game.play(difficulty_level)
    elif game == 'Guess Game':
        result = guess_game.play(difficulty_level)
    elif game == 'Currency Roulette':
        result = currency_roulette_game.play(difficulty_level)

    if result:
        print("you won")
        add_score(int(difficulty_level))
    else:
        print("you lose")





