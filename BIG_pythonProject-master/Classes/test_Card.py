from unittest import TestCase
from Card import *

class TestCard(TestCase):
    pass

    # def setUp(self):
    #     print("set up")
#tests the lowest range of card
    def test_lower_inRange(self):
        c=Card(1,1)
        self.assertEqual(c.value,1)
        self.assertEqual(c.suit,1)

    # tests the highest range of card
    def test_higher_inRange(self):
        c = Card(13, 4)
        self.assertEqual(c.value, 13)
        self.assertEqual(c.suit, 4)

    # tests the value while not in range (low)
    def test_lower_value_notInRange(self):
        try:
            c = Card(0, 1)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

    # tests the suit while not in range (low)
    def test_lower_suit_notInRange(self):
        try:
            c = Card(1, 0)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

    # tests the value while not in range (high)
    def test_higher_value_notInRange(self):
        try:
            c = Card(14, 2)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

    # tests the suit while not in range (high)
    def test_higher_suit_notInRange(self):
        try:
            c = Card(3, 5)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

    # tests the value while invalid
    def test_invalid_value(self):
        try:
            c=Card("a",3)
        except TypeError:
            self.assertTrue(True)

    # tests the suit while invalid
    def test_invalid_suit(self):
        try:
            c=Card(6 ,"b")
        except TypeError:
            self.assertTrue(True)

    # compares between cards while true
    def test_gt_betweenCards_true(self):
        c1=Card(3,1)
        c2=Card(2,1)
        self.assertTrue(c1>c2)

    # compares between cards while false
    def test_gt_betweenCards_false(self):
            c1 = Card(2, 1)
            c2 = Card(5, 1)
            self.assertFalse(c1 > c2)

    # compares between cards while not card
    def test_gt_notBetweenCarads(self):
        c=Card(1,1)
        b="string"
        try:
            c>b
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)


    def test_eq_between_cards_true(self):
        c1 = Card(1, 2)
        c2 = Card(1, 1)
        self.assertTrue(c1 == c2)

    def test_eq_between_cards_false(self):
        c1 = Card(5, 2)
        c2 = Card(1, 1)
        self.assertFalse(c1 == c2)

    def test_eq_NOTbetween_cards(self):
        c1 = Card(5, 2)
        c2 = "string"
        try:
            c1==c2
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)








