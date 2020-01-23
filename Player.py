#Player class
#Records number of letters in hand at a given time
from Letter import Letter
from Board import Board
class Player:
    def __init__(self, name):
        self.__num_letters__ = 0
        self.__score__ = 0
        self.__hand__ = []
        self.__name__ = name
        
    def get_score(self):
        return self.__score__
    def update_score(self, points):
        self.__score__ += points
        return
    def add_to_hand(self, letter):
        if not isinstance(letter, Letter):
            raise TypeError('argument is not of class Letter')
        self.__hand__.append(letter)
        self.__num_letters__ += 1
        return
    def get_hand(self):
        copy = []
        for i in range(len(self.__hand__)):
            copy.append(self.__hand__[i])
        return copy

    def get_hand_num(self):
        return self.__num_letters__
    def place_letters(self, letter, board, coords): #rename place_letter
        #queries self if a given Letter object exists
        #if so removed desired Letter from hand
        for i in range(len(self.__hand__)):
            if Letter.equals(letter, self.__hand__[i]):
                board.add_tile(coords, self.__hand__[i])
                del self.__hand__[i]
                self.__num_letters__ -= 1
                return 1
        return 0

    
                
        
        