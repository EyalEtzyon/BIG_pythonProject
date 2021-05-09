class Card:
# create new Card with value between 1-13 and suit between 1-4
    def __init__(self, value, suit):
        if 1<=value<=13 and 1<=suit<=4:
            self.value=value
        else:
            raise ValueError("ERROR")
        if 1<=suit<=4:
            self.suit = suit
        else:
            raise ValueError("ERROR")


        self.values = {1:"Ace", 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:"Jack", 12:"Queen", 13:"King"}
        self.suits = {1: "Diamond♦", 2: "Spade ♠", 3: "Heart 🖤 ", 4: "Club ♣"}


#returns the card in a user friendly way
    def __repr__(self):
        return f"{self.values[self.value]} {self.suits[self.suit]}"

#comnpares between cards
    def __gt__(self, other):
        if type(other)!=Card:
            raise ValueError("other not card")
        v1 = self.value
        v2 = other.value
        if v1 == 1:
            v1 = 14
        if v2==1:
            v2=14

        if v1>v2:
             return True
        elif v1==v2:
            if self.suit>other.suit:
                return True
            else:
                return False
        else:
            return False



