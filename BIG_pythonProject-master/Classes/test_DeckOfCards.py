from unittest import TestCase
from DeckOfCards import *


class TestDeckOfCards(TestCase):

    def setUp(self):
        print("set up")
        self.d=DeckOfCards()


    def test_shuffle(self):
       before  =self.d.deck.copy()
       self.d.shuffle()
       after = self.d.deck.copy()
       if before!=after:
            self.assertTrue(True)
       else:
            self.assertTrue(False)





    def test_deal_one(self):
        before = self.d.deck.copy()
        self.d.deal_one()
        after = self.d.deck.copy()
        if before != after:
            self.assertTrue(True)
        else:
            self.assertTrue(False)


