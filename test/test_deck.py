import pytest
import sys

sys.path.append("..")

from deck import Deck

# Tests that a deck has 4 decks of 52 cards
def test_deck_init():
    test_deck = Deck()
    assert len(test_deck.cards) == 52 * 4


# Tests that a card can be drawn
def test_draw_card():
    test_deck = Deck()
    card = test_deck.draw()

    errors = []

    if not card:
        errors.append("No card returned")

    if len(test_deck.cards) != 52 * 4 - 1:
        errors.append("Deck does not have 51 cards")

    assert not errors, "Errors occured \n{}".format("\n".join(errors))


# Tests that, if we draw more than half the deck (104 cards) that the deck will reset (ie a full shuffle)
def test_deck_min_cards():
    test_deck = Deck()

    for _ in range(105):
        test_deck.draw()

    assert len(test_deck.cards) > 52 * 2


def test_deck_reset():
    test_deck = Deck()
    test_deck.draw()
    test_deck.reset()
    assert len(test_deck.cards) == 52 * 4
