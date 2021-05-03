from Card import Card

class DeckOfCards:
    def __init__(self):
        self.deck = []
        for s in range(1,5):
            for v in range(1,14):
                card=Card(v,s)
                self.deck.append(card)

    def show(self):
        for i in self.deck:
            print(i)


deck = DeckOfCards()
deck.show()

