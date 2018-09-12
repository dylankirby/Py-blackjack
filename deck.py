"""Contains the Deck object"""
import random

class Deck(object):
    """Defines a 4 deck for playing blackjack"""
    def __init__(self):
        """Creates the deck as a standard deck times 4"""
        self.cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']*4*4

    def draw(self):
        """Draws a random card fromt the deck, 
        Resets the deck (shuffle) if more than half have been drawn
        """
        card = self.cards.pop(random.randint(0, len(self.cards)-1)) #Select random card
        if len(self.cards) < 13*4*2: # Ie more than half the deck has been dealt out
            self.reset()
            print "Deck was shuffled"
        return card

    def reset(self):
        """Returns the deck to a full 4 deck stack"""
        self.__init__()
