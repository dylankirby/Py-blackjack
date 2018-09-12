class Player(object):

	def __init__(self):
		self.bankroll = 500
		self.hand = []
		self.stay = False

	#Player makes a bet, and their banroll is reduced by that amount
	def make_bet(self, bet_amt):
		if bet_amt <= self.bankroll: 
			self.bankroll -= bet_amt
		else:
			raise ValueError("You don't have enough money for that")

	#Players hand is reset, ie at the end of the turn
	def reset_hand(self):
		self.hand = []

	def get_hand_value(self):
		card_values = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
		hand_value = sum(card_values[card] for card in self.hand)
		#IE the ace being worth 11 causes a bust
		if "A" in self.hand and hand_value > 21: 
			#reduce the value of the ace to 1 and return that value
			return hand_value-10 
		else:
			return hand_value

#Subclass of Player, has logic to check their own hand and decide if they want to hit or stay
#Also has a bankroll that will be 10X the players bankroll
class Dealer(Player):

	def __init__(self):
		Player.__init__(self)
		self.bankroll *= 10

	def evaluate_hand(self):
		value = self.get_hand_value()

		#Dealer wants to hit if the his hand is below 15
		if value < 15:
			return "hit"
		else:
			return "stay"