import random, sys

# -------- Begin definition of objects ---------------
class Player(object):

	def __init__(self, starting_amount= 500):
		self.bankroll = starting_amount

	def bet(self, bet_amount):
		self.bankroll -= bet_amount

class Game(object):

	def __init__(self):
		self.deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']*4
		self.pot = 0

	def add_to_pot(self, bet):
		self.pot += bet*2

	def choose_card(self):
		card_num = random.randint(1, len(self.deck))
		card = self.deck[card_num]
		# self.deck.pop[card_num]
		return card

	def reset(self):
		self.deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']*4
		self.pot = 0


# ----------- Global game values ------------
card_values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
game = Game()
player = Player()
player_hand = []
dealer_hand = []
stay = False

# ------------- Begin definition of functions -----------------

# This function will take the players bet, subtract it from his bankroll, and add it to the pot
def bet(bet):
	player.bet(bet)
	game.add_to_pot(bet)
	print 'You now have $ %s' %(player.bankroll)

# This function will reset the game, if the player wishes to play again. Pot set to zero, hands are emptied, and the deck is reset
def reset():
	global player_hand
	global dealer_hand
	player_hand = []
	dealer_hand = []

# This function will allow either player to hit, take that card and add it to their hand, and then print out the new table
def give_card(hand):
	hand.append(game.choose_card())

# This function will, should the player want to, start the game over, while keeping the players current bankroll
# If they don't want to play again, they can walk away with their earnings
def play_again():
	resp = raw_input("Would you like to play again? (y/n)")
	if resp.lower() == 'y':
		game.reset()
		run_game()
	else:
		print 'Thanks for playing, you walk away with $%s' %(player.bankroll)
		sys.exit()

# In the event of the player losing, this will inform them of how much they lost, and see if they want to play again
def player_loss():
	print 'Oh no, looks like you lost this round. You lost $%s, try to win it back!' %((game.pot)/2)
	play_again()

# In the event of a player win, this will tell them how much they won, add that to their bankroll, and see if they want to play again
def player_win():
	print 'Congrats player, you won! $%s has been added to your bankroll' %(game.pot)
	player.bankroll += game.pot
	play_again()

# This will check the value of a hand
def check_hand_value(hand):
	value = 0
	for card in hand:
		value += card_values[card]

	return value

# This will check to see if a hand is greater than 21 ie a bust
def check_bust(hand):
	if check_hand_value(hand) > 21:
		return True
	else:
		return False

# This will check to see, in the event no one busted, who won
def check_win(player_hand, dealer_hand):
	if check_hand_value(player_hand) > check_hand_value(dealer_hand):
		player_win()
	else:
		player_loss()

# This will print the current table for the player to see
def print_table():
	print dealer_hand[0]
	print '----------'
	for card in player_hand:
		print card,
	print ''


# This will run the game
def run_game():
	reset()
	global stay
	player_hand.append(game.choose_card())
	dealer_hand.append(game.choose_card())
	print_table()
	print ' '
	while game.pot == 0:
		try:
			bet(input('How much would you like to bet on those cards? '))
		except:
			print 'That is an invalid bet, please try again'


	while not check_bust(player_hand) and not check_bust(dealer_hand):
		# While player has not stayed, we need to take turns
		# Players turn it will ask, do you want to hit or stay
		# if hit, go to dealer, if dealer is <=15, dealer will hit
		# Return to player
		# if stay, go to dealer, if dealer is <= 15, dealer will hit
		choice = ''
		choice = (raw_input("Player, it is your turn, you can hit or stay. What'll it be? "))
		try:
			if choice.lower() == 'hit':
				give_card(player_hand)
			elif choice.lower() == 'stay':
				stay = True
		except:
			print 'You can only hit or stay, try again'
			continue
		else:
			if check_hand_value(dealer_hand) > 15 and stay == True:
				for card in dealer_hand:
					print card,

				print '----------'

				for card in player_hand:
					print card,

				check_win(player_hand, dealer_hand)
			elif check_hand_value(dealer_hand) <= 15:
				give_card(dealer_hand)
				print_table()
				continue
			else:
				print_table()
				continue

	else:
		if check_bust(player_hand):
			player_loss()
		else:
			player_win()


# Running of the actual game
print "Welcome to Python Blackjack, where all the cool kid's come to play"
run_game()





# Game will start by asking the player for an initial bet, telling them how much money they have
# This initial bet should be subtracted from their bankroll
# Will then give the player one card, and the dealer one card, and give the face value of the dealer's card
# This should print out like so
# K **** (These are the dealer's cards)
# --------
# 4 ***** (These are the player's cards)
# Program will need to keep track of the minimum count of a players cards
# Then it will ask the player if they would like to hit or stay
# If they choose hit, they will be given a card, should be added to the list of their cards and displayed to them
# The value of the card should be added to their hand value
# If they bust, there should be a message that says you busted, you lost your money
# the player should be told how much money they have, and asked if they want to play again
# # If they want to play again, The game should then start over, pot resets to 0
# if they dont bust, then the game should give the dealer a card and add to his count, 
# if the dealer busts, then the player should be notified they won, because the dealer busted
# The pot should be added to their bankroll, and reset to 0
# They should be asked if they want to play again, if so, game starts over

# Will need functions for
# 	bet
# 	stay
# 	Eval win

# Only realy need a player object, and a game object

# player object will determine how much money they player has
# game object will give us the deck and pot
