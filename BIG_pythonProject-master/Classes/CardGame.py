from Player import *
from DeckOfCards import *

class CardGame:
    def __init__(self, player_cards=10):

        self.player1=Player(input("Enter player 1 name: "), player_cards)
        self.player2=Player(input("Enter player 2 name: "), player_cards)
        self.deck = DeckOfCards()
        self.new_game()


    def new_game(self):
        self.deck.shuffle()
        self.player1.setHand(self.deck)
        self.player2.setHand(self.deck)


    def get_winner(self):



# game=CardGame()
# game.deck.show()
# game.player1.show()
# game.player2.show()
# print(len(game.deck.deck))





