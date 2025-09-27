import sys
from guess_number import guess
from rps import rps

def play_game(name = "PlayerOne"):
    welcome_back = False

    while True:
        if welcome_back == True:
            print(f"{name}, welcome back to the Arcade menu.")

        playerchoice = input("\nPlease choose a game...\n1: Rock paper scissors\n2: Guess a number\n\nOr press \"x\" to exit the arcade\n\n")

        if playerchoice not in ['1', '2', 'x']:
            print("\nYou must enter 1, 2 or x")
            return play_game(name)
        
        welcome_back = True

        if playerchoice == "1":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif playerchoice == "2":
            guess_game = guess(name)
            guess_game()
        else:
            print("\nSee you next time!")
            sys.exit(f"Bye {name}!")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description = "Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar = "name",
        required=True, help = "The name of the player."
    )

    args = parser.parse_args()

    print(f"\n{args.name}, welcome to the Arcade! 🤖")

    play_game(args.name)