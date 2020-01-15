#Game object
#TODO: Hardcode values 
from Player import Player
from Letter import Letter
from Board import Board
BONUS_COORDS = [(1, 1, '3w'), (1, 4, '2l'), (1, 8, '3w'), (1, 12, '2l'), (1, 15, '3w'),
                (2, 2, '2w'), (2, 6, '3l'), (2, 10, '3l'), (2, 14, '2w'),
                ()]
TILE_DIST = [('A', 9), ('B', 2), ('C', 2), ('D', 4), ('E', 12), ('F', 2), ('G', 3), ('H', 2), ('I', 9), ('J', 1), ('K', 1), ('L', 4), ('M', 2), ('N', 6),
            ('O', 8), ('P', 2), ('Q', 1), ('R', 6), ('S', 4), ('T', 6), ('U', 4), ('V', 2), ('W', 2), ('X', 1), ('Y', 2), ('Z', 1), ('BLANK', 2)]
class Game:
    def __init__ (self):
        #initialize board and player objects
        #initialize a list of Letter objects
        self.tile_bag = []
        self.tile_bag_count = 0
        for j in range(len(TILE_DIST)):
            for k in range(TILE_DIST[j][1]):
                self.tile_bag.append(Letter(TILE_DIST[j][0]))
                self.tile_bag_count += 1
    def __turn__(self):
        #prompt for Letter input, take from Player's hand
        #end of turn, add missing Letters to Player's hand
        pass

    def give_letter(self, player):
        #pop a Letter from local Letter stack and send it to the Player object
        pass

    def give_hand (self, player):
        #give player seven Letters
        pass

    def get_tile_bag(self):
        return self.tile_bag.copy()

    def get_tile_bag_count(self):
        return self.tile_bag_count
