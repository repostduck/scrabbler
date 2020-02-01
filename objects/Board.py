


class Tile:
    def __init__ (self, letter):
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
        elif(letter == '_'):
            self.__points__ = 0
        else:
            raise ValueError('not an acceptable letter value')
        
    

    def set_letter(self, letter):
        if not self.inhabited():
            self.__letter__ = letter
            self.__points__ = letter.get_points()
            self.__inhabited__ = 1
            return 1
        return 0

    def get_letter(self):
        if self.__letter__ == "BLANK":
            return '?'
        return self.__letter__
        
    def is_inhabited(self):
        return self.__letter__ != '_'

    def get_points(self):
        return self.__points__

    def set_points(self):
        return self.__points__

    def view(self):
        return dict([
            ('letter', self.get_letter()),
            ('points', self.get_points())
        ])
        
    @classmethod
    def equals(cls, eq1, eq2):
        if (eq1.get_letter() == eq2.get_letter()):
            return 1
        else:
            return 0



#initialize a grid of 15 x 15 tiles and assign values to each
#parameter: bonusCoords is a list acting as a stack containing (x,y) values
class Board:
    def __init__ (self, bonus_coords=[]):
        self.grid = []
        for x in range(15):
            self.grid.append([])
            for y in range(15):
                self.grid[x].append(dict({'tile': Tile('_')}))
                self.grid[x][y].update({'bonus': 'Normal'})
        for i in range(len(bonus_coords)):
            self.grid[bonus_coords[i][0] - 1][bonus_coords[i][1] - 1]['bonus'] = bonus_coords[i][2]

    def add_tile (self, coord, letter):
        #assign Tile to the designated space in grid
        #remove previous Tile
        temp = self.grid[coord[0]][coord[1]]['tile']
        self.grid[coord[0]][coord[1]].update({'tile' : letter})
        del temp
    def print(self):
        for i in range(15):
            line = ''
            for j in range(15):
                if (self.grid[i][j]['tile'].is_inhabited() == 0):
                    temp = "_"
                    line += temp.center(3, ' ')
                else:
                    line += ((str)(self.grid[i][j]['tile'].get_letter())).center(3, ' ')
            print(line)
        return 0

    #returns the tile at a given coordinate on the board
    def get_tile(self, coord):
        return self.grid[coord[0]][coord[1]]['tile']