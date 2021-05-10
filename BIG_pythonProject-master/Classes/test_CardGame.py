from unittest import TestCase
from Player import *
from CardGame import *
from DeckOfCards import *

class TestCardGame(TestCase):

    def setUp(self):
        print("set up")
        self.game = CardGame("Eyal","guy")


    def test_new_game(self):
        before = len(self.game.deck.deck)
        self.game.new_game()
        after=len(self.game.deck.deck)
        self.assertEqual(before,after)

    # testing when player1 is the winner (has the smaller hand)
    def test_get_winner_player1Wins(self):
        self.game.player2.hand.append(Card(1, 1))
        self.assertEqual(self.game.player1, self.game.get_winner())

    # testing when player2 is the winner (has the smaller hand)
    def test_get_winner_player2Wins(self):
        self.game.player1.hand.append(Card(1, 1))
        self.assertEqual(self.game.player2, self.game.get_winner())

    # testing when the players has the same hand's len
    def test_get_winner_Tie(self):
        self.assertEqual(None, self.game.get_winner())






