# guessing game where you have to guess the number the computer is thinking of

import sys
import random

def guess(name = "PlayerOne"):
    game_count = 0
    player_wins = 0

    def guess_number():
        nonlocal player_wins

        playerchoice = input(f"\n{name}, guess which number I'm thinking of... 1, 2, or 3.\n\n")

        if playerchoice not in ['1', '2', '3']:
            print("\nYou must enter 1, 2 or 3")
            return guess_number()

        player = int(playerchoice)

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print(f"\n{name}, you chose {player}")
        print(f"\nI was thinking of the number {computer}\n")

        def decide_winner(player):
            nonlocal name
            nonlocal player_wins
            
            if player == computer:
                player_wins += 1
                return f"{name}, you win"
            else:
                return f"Sorry, {name}. Better luck next time"
        
        game_result = decide_winner(player)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nYour winning percentage: {player_wins / game_count:.2%}")

        print(f"\nPlay again, {name}?")

        while True:
            play_again = input("\nY for Yes or\nQ for Quit\n")
            if play_again.lower() not in ["y", "q"]:
                continue
            else:
                break

        if play_again == "y":
            return guess_number()
        else:
            print("\n🥳🥳🥳")
            print("Thank you for playing")
            if __name__ == "__main__":  # handles whether file is launched itself or from the arcade
                sys.exit(f"Bye {name}!")
            else:
                return
            
    return guess_number

# getting command line argument for my name
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description = "Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar = "name",
        required=True, help = "The name of the person playing the game."
    )

    args = parser.parse_args()

    guess_game = guess(args.name)
    guess_game()