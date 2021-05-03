class Card:

    def __init__(self, value, suit):
        if 1<=value<=13:
            self.value=value
        else:
            print("ERROR")
            if 1<=suit<=4:
                self.suit = suit
            else:
                print("ERROR")


        self.values = {1:"Ace", 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:"Jack", 12:"Queen", 13:"King"}
        self.suits = {1: "Diamond♦", 2: "Spade ♠", 3: "Heart 🖤 ", 4: "Club ♣"}



    def __repr__(self):
        return f"{self.values[self.value]} {self.suits[self.suit]}"

    def __gt__(self, other):
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



