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
        copy = []
        for i in range(len(self.__hand__)):
            copy.append(self.__hand__[i])
        return copy
    def askLetters(self, letter):
        #queries self if a given Letter object exists (index, pop)
        #if so pop desired Letter from List
        #if (not isinstance(letter, Letter)):
        #    return None
       # else:
           # for i in range(len(self.__hand__)):
        pass
        
        