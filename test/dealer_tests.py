"""Tests for the dealer module"""
import sys
import pytest

sys.path.append('..')

from player import Dealer
from deck import Deck

#Tests that the dealer will have a bankroll of 5000, 10x the standard player bankroll
def test_dealer_bankroll():
    """Tests the initilization of the dealers bankroll"""
    test_dealer = Dealer()
    assert test_dealer.bankroll == 500*10

# Tests that the dealer will decide to hit (hand value below 15) or stay appropriately
@pytest.mark.repeat(500)
def test_dealer_decision():
    """Tests dealers hit/stay decision mechanics"""
    card_values = {
        'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, 
        '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10
        }
    test_dealer = Dealer()
    test_deck = Deck()

    hand_value = 0

	#Will draw two cards, place them in the dealers hand, updating hand value
    for _ in range(2):
        card = test_deck.draw()
        test_dealer.hand.append(card)
        hand_value += card_values[card]

    if hand_value < 15:
        assert test_dealer.evaluate_hand() == "Hit"
    else:
        assert test_dealer.evaluate_hand() == "Stay"

