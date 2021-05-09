from unittest import TestCase
from Player import *
from unittest import mock
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






    # def test_set_hand(self):
    #     self.fail()
    #
    # def test_get_card(self):
    #     self.fail()
    #
    # def test_add_card(self):
    #     self.fail()
    #
    # def test_show(self):
    #     self.fail()
