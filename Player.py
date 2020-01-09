#Player class
#Records number of letters in hand at a given time
from Letter import Letter
class Player:
    def __init__(self, name):
        self.__numLetters__ = 0
        self.__score__ = 0
        self.__hand__ = []
        self.__name__ = name
        
    def getScore(self):
        return int(self.__score__)
    def updateScore(self, points):
        self.__score__ += points
        return
    def addToHand(self, letter):
        if not isinstance(letter, Letter):
            raise TypeError('argument is not of class Letter')
        self.__hand__.append(letter)
        self.__numLetters__ += 1
        return
    def getHand(self):
        copy = self.__hand__.copy()
        return copy

