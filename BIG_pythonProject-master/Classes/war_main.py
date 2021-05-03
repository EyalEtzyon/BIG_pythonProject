from CardGame import *
from Player import *
from Card import *
game = CardGame()
game.player1.show()
game.player2.show()


for i in range(10):
    card1= game.player1.get_card()
    print(game.player1.name+": ", card1)
    card2= game.player2.get_card()
    print(game.player2.name+": ", card2)
    if card1>card2:
        game.player2.add_card(card1)
        game.player2.add_card(card2)
        print("winner: ", game.player1.name)
    else:
        game.player1.add_card(card2)
        game.player1.add_card(card1)
        print("winner: ", game.player2.name)



if len(game.player1.hand)> len(game.player2.hand):
    print(game.player2.name,"is the WINNER!")
elif len(game.player2.hand)> len(game.player1.hand):
        print(game.player1.name,"is the WINNER!")
else: print("ITS A TIE")







