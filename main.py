"""Runs a new instance of the blackjack game"""
from game import Game

def main():
    """Starts the game, listens for keyboard interrupt"""
    game = Game()
    try:
        game.new_round()
    except KeyboardInterrupt:
        print "Exiting program"

if __name__ == "__main__":
    main()
