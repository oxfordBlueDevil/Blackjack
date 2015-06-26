from blackjack_player import BlackjackPlayer
from deck import BlackjackDeck
from blackjack_hand import BlackjackHand

import nose.tools as n

def test_card_init():
    card = BlackjackCard("J", "s")
    n.assert_equal(card.number, "J")
    n.assert_equal(card.suit, "s")

def test_radd():
    card1 = BlackjackCard("A","s")
    card2 = BlackjackCard("8","d")
    card3 = BlackjackCard("9","s")
    cards = [card1, card2, card3]
    n.assert_equal(sum(cards), 18)

def test_deck_init():
    deck = BlackjackDeck()
    n.assert_equal(len(deck), 52)
    card = deck.draw_card()
    n.assert_equal(card.value_dict['Q'], 10)

def test_shuffle():
    deck = BlackjackDeck()
    card = deck.draw_card()
    n.assert_equal(len(deck), 51)
    deck.shuffle()
    n.assert_equal(len(deck), 52)

