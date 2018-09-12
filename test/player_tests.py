import sys
import pytest

sys.path.append('..')

from player import Player
from deck import Deck

# Tests that a new player has a bankroll attribute, deafaults to 500
def test_bankroll_init(): 
	test_player = Player()
	assert test_player.bankroll == 500

# Tests that a player can make a bet, and his banroll will be reduced by that amount
def test_bet_function(): 
	starting_bankroll = 500
	bet = 200

	test_player = Player()
	test_player.make_bet(bet)

	assert test_player.bankroll == starting_bankroll - bet

def test_stay():
	test_player = Player()
	assert not test_player.stay

# Test that a player can have their hand reset
def test_reset_hand(): 
	test_player = Player()
	test_deck = Deck()

	test_player.hand.append(test_deck.draw())
	test_player.reset_hand()

	assert len(test_player.hand) == 0

@pytest.mark.repeat(500)
def test_hand_value():
	card_values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
	test_player = Player()
	test_deck = Deck()

	hand_value = 0

	for _ in range(2):
		card = test_deck.draw()
		hand_value += card_values[card]
		test_player.hand.append(card)

	assert test_player.get_hand_value() == hand_value

