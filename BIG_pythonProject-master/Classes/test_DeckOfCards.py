from unittest import TestCase
from DeckOfCards import *


class TestDeckOfCards(TestCase):

    def setUp(self):
        print("set up")
        self.d=DeckOfCards()


    def test_shuffle(self):
       before  =self.d.deck
       self.d.shuffle()
       after = self.d.deck
       self.assertNotEqual()




    def test_show(self):
        self.fail()



    def test_deal_one(self):
        self.fail()
