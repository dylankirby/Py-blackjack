"""This method contains all classes related to different players in a Blackjack game"""

class Player(object):
    """Defines a Player in the game"""

    def __init__(self):
        """Sets the bankroll (500), hand (empty list), and stay (false) attributes"""
        self.bankroll = 500
        self.hand = []
        self.stay = False

    def make_bet(self, bet_amt):
        """Deducts the players bet amount from their bankroll if they have the funds"""
        if bet_amt <= self.bankroll: 
            self.bankroll -= bet_amt
        else:
            raise ValueError("You don't have enough money for that")

    #Players hand is reset, ie at the end of the round
    def reset_hand(self):
        """Resets the players hand to an empty list"""
        self.hand = []

    #Gets the value of a hand with ace valued at 11, if this causes a bust, changes value to 1
    def get_hand_value(self):
        """Will return the counted value of a hand"""
        card_values = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, 
                       '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
        hand_value = sum(card_values[card] for card in self.hand)
		
        #If ace = 11 causes bust
        if "A" in self.hand and hand_value > 21: 
            #reduce the value of the ace to 1 and return that value
            return hand_value-10 
        else:
            return hand_value

#Subclass of Player, has logic to check their own hand and decide if they want to hit or stay
#Also has a bankroll that will be 10X the players bankroll
class Dealer(Player):
    """Defines the Dealer subclass, inheriting from the Player superclass"""

    def __init__(self):
        """Sets the dealer bankroll to 10 times a players bankroll"""
        Player.__init__(self)
        self.bankroll *= 10

    #Dealer will hit if hand is less than 15, stay if it is equal or greater than 15
    def evaluate_hand(self):
        """Will return hit or stay based on the dealers current hand"""
        value = self.get_hand_value()

		#Dealer wants to hit if the his hand is below 15
        if value < 15:
            return "hit"
        else:
            return "stay"
