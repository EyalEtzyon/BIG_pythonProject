from CardGame import *
from Player import *
from Card import *
game = CardGame(input("Name of player 1: "), input("Name of player2: "))
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



#  task 7
if game.get_winner()==game.player2:
    print(f"The Winner Is... {game.player2.name}!!!")
if game.get_winner()==game.player1:
    print(f"The Winner Is... {game.player1.name}!!!")
if game.get_winner()==None:
    print("Fair Fight.. It's a TIE!!!")








