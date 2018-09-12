import sys
import pytest

sys.path.append('..')

from game import Game


def test_game_init():
	test_game = Game()

	errors = []

	if not test_game.player:
		errors.append("No Player found")

	if not test_game.dealer:
		errors.append("No dealer found")

	if not test_game.deck:
		errors.append("No deck found")

	if not test_game.pot == 0:
		errors.append("Game pot is not 0 at start")

	assert not errors, "Errors Occured \n{}".format("\n".join(errors))

#Checks that a bet can be made by deducting the bet amount from both player and dealer, and adding that money to the pot
def test_make_bet():
	test_game = Game()
	bet_amt = 200
	test_game.take_bet(bet_amt)

	errors = []

	if test_game.player.bankroll != (500-bet_amt):
		errors.append("Player bankroll not adjusted")

	if test_game.dealer.bankroll != (500*10 - bet_amt):
		errors.append("Dealer bankroll not adjusted")

	if test_game.pot != bet_amt*2:
		errors.append("Pot is not twice the bet amount")

	assert not errors, "Errors Occured \n{}".format("\n".join(errors))

#Test that if a player busts, the game will correctly identify this
def test_check_bust():
	test_game = Game()

	cards = ["J", "Q", "K"]

	for card in cards:
		test_game.player.hand.append(card)

	assert test_game.check_bust(test_game.player)

#Tests that game can evaluate both hands once players have stayed and determine the winner
def test_check_win():
	test_game = Game()

	dealer_cards = ["J", "3"]
	player_cards = ["A", "J"]

	for card in dealer_cards:
		test_game.dealer.hand.append(card)

	for card in player_cards:
		test_game.player.hand.append(card)

	assert test_game.check_win()
