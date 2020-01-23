#Game object
from Player import Player
from Board import Board
from Board import Tile
import random
#bonus coords list is indexed from 1-15
BONUS_COORDS = [(1, 1, '3w'), (1, 4, '2l'), (1, 8, '3w'), (1, 12, '2l'), (1, 15, '3w'),
                (2, 2, '2w'), (2, 6, '3l'), (2, 10, '3l'), (2, 14, '2w'),
                (3, 3, '2w'), (3, 7, '2l'), (3, 9, '2l'), (3, 13, '2w'),
                (4, 1, '2l'), (4, 4, '2w'), (4, 8, '2l'), (4, 12, '2w'), (4, 15, '2l'),
                (5, 5, '2w'), (5, 11, '2w'),
                (6, 2, '3l'), (6, 6 ,'3l'), (6, 10, '3l'), (6, 14, '3l'),
                (7, 3, '2l'), (7, 7, '2l'), (7, 9, '2l'), (7, 13, '2l'),
                (8, 1, '3w'), (8, 4, '2l'), (8, 8, '2w'), (8, 12, '2l'), (8, 15, '3w'),
                (9, 3, '2l'), (9, 7, '2l'), (9, 9, '2l'), (9, 13, '2l'),
                (10, 2, '3l'), (10, 6, '3l'), (10, 10, '3l'), (10, 14, '3l'),
                (11, 5, '2w'), (11, 11, '2w'),
                (12, 1, '2l'), (12, 4, '2w'), (12, 8, '2l'), (12, 12, '2w'), (12, 15, '2l'),
                (13, 3, '2w'), (13, 7, '2l'), (13, 9, '2l'), (13, 13, '2w'),
                (14, 2, '2w'), (14, 6, '3l'), (14, 10, '3l'), (14, 14, '2w'),
                (15, 1, '3w'), (15, 4, '2l'), (15, 8, '3w'), (15, 12, '2l'), (15, 15, '3w')]

TILE_DIST = [('A', 9), ('B', 2), ('C', 2), ('D', 4), ('E', 12), ('F', 2), ('G', 3), ('H', 2), ('I', 9), ('J', 1), ('K', 1), ('L', 4), ('M', 2), ('N', 6),
            ('O', 8), ('P', 2), ('Q', 1), ('R', 6), ('S', 4), ('T', 6), ('U', 4), ('V', 2), ('W', 2), ('X', 1), ('Y', 2), ('Z', 1), ('BLANK', 2)]
class Game:
    def __init__ (self):
        #initialize board and player objects
        #initialize a list of Letter objects
        self.__tile_bag__ = []
        self.__tile_bag_count__ = 0
        for j in range(len(TILE_DIST)):
            for k in range(TILE_DIST[j][1]):
                self.__tile_bag__.append(Tile(TILE_DIST[j][0]))
                self.__tile_bag_count__ += 1
        self.__board__ = Board(self, BONUS_COORDS)

    def __turn__(self):
        #prompt for Letter input, take from Player's hand
        #end of turn, add missing Letters to Player's hand
        pass

    def give_letter(self, player):
        #pop a Letter from local Letter stack and send it to the Player object
        if self.__tile_bag_count__ <= 0:
            return
        else:
            randnum = random.randint(0, self.get_tile_bag_count() - 1)
            player.add_to_hand(self.__tile_bag__[randnum])
            del self.__tile_bag__[randnum]
            self.__tile_bag_count__ -= 1
            return

    def give_hand (self, player):
        #give player seven Letters
        #need to randomize
        for i in range(7):
            self.give_letter(player)
        return

    def get_tile_bag(self):
        return self.__tile_bag__.copy()

    def get_tile_bag_count(self):
        return self.__tile_bag_count__

    def get_board(self):
        return self.__board__
