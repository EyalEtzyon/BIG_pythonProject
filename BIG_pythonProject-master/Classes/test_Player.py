from unittest import TestCase
from Player import *
from unittest import mock
from unittest.mock import patch



class TestPlayer(TestCase):

#test invalid name
    def test_name_invalid(self):
        try:
            p = Player(123)
            self.assertTrue(False)
        except: TypeError("not a string")
        self.assertTrue(True)
#test valid name
    def test_name_valid(self):
            p = Player("eyal")
            self.assertTrue(p.name=="eyal")
            self.assertTrue(p.cardsNum==10)

#test invalid input oc cards number
    def test_CardsNum_invalid(self):
        try:
            p = Player("Eyal","string")
            self.assertTrue(False)
        except TypeError:
                self.assertTrue(True)

#test max cars num not in range
    def test_CardsNum_invalid_num_min(self):
        try:
            p = Player("E", -1)
            self.assertTrue(False)
        except TypeError:
            self.assertTrue(True)

#test max cars num not in range
    def test_CardsNum_invalid_num_max(self):
            p = Player("Eyal", 27)
            self.assertTrue(p.cardsNum==26)

#test min cars num in range
    def test_CardsNum_valid_num_min(self):
            p = Player("E", 0)
            self.assertTrue(p.cardsNum==0)


        # test max cars num in range
    def test_CardsNum_valid_num_max(self):
        p = Player("Eyal", 26)
        self.assertTrue(p.cardsNum == 26)





    @mock.patch("DeckOfCards.DeckOfCards.deal_one", return_value=Card(1,1))
    def test_set_hand(self, mock_deal_one):
            Eyal = Player("Eyal", 3)
            deck = DeckOfCards()
            Eyal.setHand(deck)
            self.assertIn(Card(1,1), Eyal.hand)
            self.assertEqual(Eyal.hand.count(Card(1,1)),3)













    def test_get_card(self):
        Eyal = Player("Eyal",2)
        Eyal.hand = [Card(1,1),Card(2,1)]
        before = Eyal.hand.copy()
        c = Eyal.get_card()
        self.assertTrue(type(c)==Card)
        after = Eyal.hand.copy()
        if c not in after and c in before:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

        # testing the hand after we add card.
        # if the card is in the hand after we add it, the test will pass.
    def test_add_card(self):
            Eyal = Player("Eyal")
            Eyal.add_card(Card(3, 3))
            after = Eyal.hand.copy()
            if Card(3, 3) in after:
                self.assertTrue(True)
            else:
                self.assertTrue(False)



