class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


        self.values = {1:"Ace", 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:"Jack", 12:"Queen", 13:"King" }
        self.suits = {1: "Diamond♦", 2: "Spade ♠", 3: "Heart 🖤 ", 4: "Club ♣"}



    def __repr__(self):
        return f"{self.values[self.value]} {self.suits[self.suit]}"

