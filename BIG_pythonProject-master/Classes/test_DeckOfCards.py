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



    def test_constractor(self):
        for s in range(1,5):
            for v in range(1,14):
                card = Card(v,s)
                if card not in self.d.deck:
                    self.assertTrue(False)
        else:
                    self.assertTrue(True)

    def test_deal_one(self):
        before = self.d.deck.copy()
        c=self.d.deal_one()
        self.assertTrue(type(c)==Card)
        after = self.d.deck.copy()
        if c in before and c not in after:
            self.assertTrue(True)
        else:
            self.assertTrue(False)





