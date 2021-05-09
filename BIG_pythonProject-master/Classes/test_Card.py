from unittest import TestCase
from Card import *

class TestCard(TestCase):
    pass

    def setUp(self):
        print("set up")

    def test_lower_inRange(self):
        c=Card(1,1)
        self.assertEqual(c.value,1)
        self.assertEqual(c.suit,1)



    def test_higher_inRange(self):
        c = Card(13, 4)
        self.assertEqual(c.value, 13)
        self.assertEqual(c.suit, 4)

    def test_lower_value_notInRange(self):
        try:
            c = Card(0, 1)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

    def test_lower_suit_notInRange(self):
        try:
            c = Card(1, 0)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

    def test_higher_value_notInRange(self):
        try:
            c = Card(14, 2)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

    def test_higher_suit_notInRange(self):
        try:
            c = Card(3, 5)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)


    def test_invalid_value(self):
        try:
            c=Card("a",3)
        except TypeError:
            self.assertTrue(True)

    def test_invalid_suit(self):
        try:
            c=Card(6 ,"b")
        except TypeError:
            self.assertTrue(True)


    def test_gt_betweenCards_true(self):
        c1=Card(3,1)
        c2=Card(2,1)
        self.assertTrue(c1>c2)



    def test_gt_betweenCards_false(self):
            c1 = Card(2, 1)
            c2 = Card(5, 1)
            self.assertFalse(c1 > c2)


    def test_gt_notBetweenCarads(self):
        c=Card(1,1)
        b="string"
        try:
            c>b
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)








