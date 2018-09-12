import sys
from player import Player, Dealer
from deck import Deck

#Game class defines the game as a whole, which should have a player, a dealer, a deck, and a table (represented by the pot)
class Game(object):
	
	# Initialize game with a player, dealer, pot, and a deck
	def __init__(self):
		self.deck = Deck() #Game has a deck
		self.player = Player() #Game has a player
		self.dealer = Dealer() #Game has a dealer
		self.pot = 0 #Game has a pot

	#Takes a bet amount and will deduct that amount from the player and the dealer, and place it into the pot
	def take_bet(self, bet_amt):
		self.player.make_bet(bet_amt)
		self.dealer.make_bet(bet_amt)
		self.pot += bet_amt*2
		print "You now have $%s" %(self.player.bankroll)
		print "Pot is worth $%s \n" %(self.pot)


	#Will print the table to show the user where he stands, and the first card of the dealer
	def print_table(self):
		try:
			print self.dealer.hand[0]
			print '----------------'
			for card in self.player.hand:
				print card,
		except IndexError:
			pass
		print "\n"

	#Prints the full table so the player can see who won
	def print_table_final(self):
		for card in self.dealer.hand:
			print card
		print '----------------'
		for card in self.player.hand:
			print card
		print "\n"

	#Check if a player passed to the function has busted
	def check_bust(self, player_to_check):
		if player_to_check.get_hand_value() <= 21:
			return False
		return True

	#Starts a new round of the game, ie a new hands, new bets
	def new_round(self):
		#Reset hands, pot, and stay status for player and dealer
		self.player.reset_hand()
		self.player.stay = False
		self.dealer.reset_hand()
		self.dealer.stay = False
		self.pot = 0

		#Deal first cards to both
		self.player.hand.append(self.deck.draw())
		self.dealer.hand.append(self.deck.draw())

		#Print table and player bankroll and take bet
		self.print_table()
		print "You have $%s" %(self.player.bankroll)

		#Loop until a bet is made
		while self.pot == 0:
			try:
				self.take_bet(input('How much would you like to bet on those cards? \n'))
			except Exception as e:
				print e
		
		#Start first turn of the game
		self.game_turn()

	def play_again_question(self):
		#Until break, force player to put y/n
		while True:	
			play_again = raw_input("Another hand? [y/n]")
			play_again = play_again.lower()
			try:
				if play_again == "y":
					break
				elif play_again == "n":
					print "You walk away with $%s" %(self.player.bankroll)
					sys.exit()
				else:
					raise ValueError("Yes (y) or No (n)?")
			except Exception as e:
				print e

		self.new_round()

	#Logic for handling the player winning a hand
	def player_win(self):
		#Add winnings to player bankroll
		self.player.bankroll += self.pot

		#Print table, and inform player of win
		self.print_table_final()
		print "You won this round! $%s has been added to your bankroll" %(self.pot)

		#Check if player wants to player again
		self.play_again_question()

	#Logic for dealer winning a hand, ie player lost
	def dealer_win(self):
		#Add winnings to dealers bankroll
		self.dealer.bankroll += self.pot

		#Print table and inform player that he lost
		self.print_table_final()
		print "You lost this hand"
		
		#Check if player wants to play again
		if self.player.bankroll > 0:
			self.play_again_question()
		else:
			print "You're all out of cash, come back another time"
			sys.exit()

	#Check win and handle that
	def check_win(self):
		if self.player.get_hand_value() > self.dealer.get_hand_value():
			self.player_win()
		else:
			self.dealer_win()

	#One turn of the game, check if the player wants to hit/stay, deal card, check bust, and repeat for the dealer
	def game_turn(self):
		#Print table for player to see
		self.print_table()

		#Player turn logic

		#Player has not stayed
		if not self.player.stay: 
			while True:
				#Get player choice on hit/stay
				choice = (raw_input("It's your turn, do you want to hit or stay \n"))
				choice = choice.lower()
				try:
					if choice == "hit":
						#Add card to players hand
						self.player.hand.append(self.deck.draw())
						break
					elif choice == "stay":
						#Set stay to true
						self.player.stay = True
						break
					else: #Input was not hit or stay
						raise ValueError("You can only hit or stay \n")
				except Exception as e:
					print e
					continue

			#Check bust after players turn
			if self.check_bust(self.player):
				self.dealer_win()

		#Dealer turn Logic
		if not self.dealer.stay: #Dealer has not stayed
			if self.dealer.evaluate_hand() == "hit":
				self.dealer.hand.append(self.deck.draw())

				if self.check_bust(self.dealer):
					#Dealer has busted on this card
					self.player_win()

			else:
				self.dealer.stay = True

		if self.dealer.stay == True and self.player.stay == True:
			#Game is over, evaluate for winner
			self.check_win()
		else:
			#Take another turn of the game
			self.game_turn()



			
