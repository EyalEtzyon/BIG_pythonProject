class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


    def __repr__(self):
        return f"value: {self.value} suit: {self.suit}"

