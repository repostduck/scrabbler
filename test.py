from Player import Player
from Letter import Letter
from Game import Game
from Board import Board

#1. test Letter.equals
a = Letter('Q')
b = Letter('A')
print(Letter.equals(a, b))

#2. initialize Player object, add Letters to its hand
carl = Player('Carl')
carl.add_to_hand(a)
carl.add_to_hand(b)
tiles = carl.get_hand()
for i in range(len(tiles)):
    print(tiles[i].get_letter())

#3 initialize Game object, generate scrabble letter distribution
game = Game()
print(game.get_tile_bag_count())

#4 initialize Player object, have the Game give the Player a starting hand
steve = Player('Steve')
game.give_hand(steve)
print(steve.get_hand_num())
print(game.get_tile_bag_count())
for i in range(len(steve.get_hand())):
    print(steve.get_hand()[i].view())

#5 initialize Board object, stick a Letter object on a tile
#write a Board.print method
board = Board(game, [])
board.add_tile([0,0], a)
board.add_tile([14,0], Letter('G'))
board.add_tile([14,1], Letter('R'))
board.add_tile([14,2], Letter('E'))
board.add_tile([14,3], Letter('A'))
board.add_tile([14,4], Letter('T'))
board.add_tile([10,10], Letter('BLANK'))

#6 place a Letter from a Player's hand onto a Tile on the Board
steve.place_letters(steve.get_hand()[0], board, [2,2])
board.print()
#7 place three Letters from a Player's hand onto Tiles on the Board, calculate scoring

#8 add a blank tile to the board and prompt for letter, have game calculate score



print(a.get_letter())
aa = a.get_letter().center(3, ' ') + b.get_letter().center(3, ' ')
print(aa)

