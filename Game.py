#Game object
#TODO: Hardcode values 
from Player import Player
from Letter import Letter
from Board import Board
BONUS_COORDS = [(1, 1, '3w'), (1, 4, '2l'), (1, 8, '3w'), (1, 12, '2l'), (1, 15, '3w'),
                (2, 2, '2w'), (2, 6, '3l'), (2, 10, '3l'), (2, 14, '2w'),
                ()]
class Game:
    def __init__ (self):
        #initialize board and player objects
        #initialize a list of Letter objects
        pass
    def __turn__(self):
        #prompt for Letter input, take from Player's hand
        #end of turn, add missing Letters to Player's hand
        pass

    def __give_letter__(self, player):
        #pop a Letter from local Letter stack and send it to the Player object
        pass

    def __give_hand__ (self, player):
        #give player seven Letters
        pass
