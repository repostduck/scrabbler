from Player import Player
from Letter import Letter
from Game import Game

#1. test Letter.equals
a = Letter('Q')
b = Letter('A')
print(Letter.equals(a, b))

#2. initialize Player object, add Letters to its hand
carl = Player('Carl')
carl.addToHand(a)
carl.addToHand(b)
tiles = carl.getHand()
for i in range(len(tiles)):
    print(tiles[i].getPoints())

#3 initialize Game object, generate scrabble letter distribution
game = Game()
print(game.get_tile_bag_count())

