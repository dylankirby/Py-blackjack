import random

class Deck(object):

	def __init__(self):
		self.cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']*4*4 #4 Deck Blackjack

	def draw(self):
		card = self.cards.pop(random.randint(0,len(self.cards)-1)) #Select random card
		if(len(self.cards) < 13*4*2): # Ie more than half the deck has been dealt out
			self.reset()
			print "Deck was shuffled"
		return card

	def reset(self):
		self.__init__()