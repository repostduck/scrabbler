#Letter class
#Determines and records point value and type of letter

class Letter:
    def __init__(self, letter):
        self.__letter__ = letter
        if (letter == 'A'):
            self.__points__ = 1
        elif(letter == 'B'):
            self.__points__ = 3
        elif(letter == 'C'):
            self.__points__ = 3
        elif(letter == 'D'):
            self.__points__ = 2
        elif(letter == 'E'):
            self.__points__ = 1
        elif(letter == 'F'):
            self.__points__ = 4
        elif(letter == 'G'):
            self.__points__ = 2
        elif(letter == 'H'):
            self.__points__ = 4
        elif(letter == 'I'):
            self.__points__ = 1
        elif(letter == 'J'):
            self.__points__ = 8
        elif(letter == 'K'):
            self.__points__ = 5
        elif(letter == 'L'):
            self.__points__ = 1
        elif(letter == 'M'):
            self.__points__ = 3
        elif(letter == 'N'):
            self.__points__ = 1
        elif(letter == 'O'):
            self.__points__ = 1
        elif(letter == 'P'):
            self.__points__ = 3
        elif(letter == 'Q'):
            self.__points__ = 10
        elif(letter == 'R'):
            self.__points__ = 1
        elif(letter == 'S'):
            self.__points__ = 1
        elif(letter == 'T'):
            self.__points__ = 1
        elif(letter == 'U'):
            self.__points__ = 1
        elif(letter == 'V'):
            self.__points__ = 4
        elif(letter == 'W'):
            self.__points__ = 4
        elif(letter == 'X'):
            self.__points__ = 8
        elif(letter == 'Y'):
            self.__points__ = 4
        elif(letter == 'Z'):
            self.__points__ = 10
        elif(letter == 'BLANK'):
            self.__points__ = 0
        else:
            raise ValueError('not an acceptable letter value')
    
    def getLetter(self):
        return self.__letter__

    def getPoints(self):
        return self.__points__

    def view(self):
        return dict([
            ('letter', self.getLetter()),
            ('points', self.getPoints())
        ])
    

