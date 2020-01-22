from Letter import Letter


class Tile:
    def __init__ (self):
        self.letter = None
        self.bonus = 'Normal'
        self.inhabited = 0
        self.score = 0

    def set_bonus(self, value):
        if not (value == 'Normal' or value == '3l' or value == '3w' or value == '2l' or value == '2w'):
            raise ValueError("inappropriate bonus value phrase")
        else:
            self.bonus = value
        return
    def get_bonus(self):
        return self.bonus

    def set_letter(self, letter):
        if self.inhabited == 0:
            self.letter = letter
            self.score = letter.get_points()
            self.inhabited = 1
            return 1
        return 0

    def get_letter(self):
        if self.letter.get_letter() == "BLANK":
            return '?'
        return self.letter.get_letter()
    def is_inhabited(self):
        return self.inhabited

#initialize a grid of 15 x 15 tiles and assign values to each
#parameter: bonusCoords is a list acting as a stack containing (x,y) values
class Board:
    def __init__ (self, game, bonus_coords):
        self.grid = dict()
        for x in range(15):
            for y in range(15):
                self.grid[(x,y)] = Tile()
        self.game = game
        for i in range(len(bonus_coords)):
            self.grid[(bonus_coords[i][0] - 1, bonus_coords[i][1] - 1)].set_bonus(bonus_coords[i][2])

    def add_tile (self, coord, letter):
        #assign the Letter to the designated tile
        #return tuple of 1. calculated (2l, 3l) score and 2. type of multiplier (normal, 2w, 3w)
        #removes existing bonus if any
        self.grid[(coord[0], coord[1])].set_letter(letter)

    def print(self):
        for i in range(15):
            line = ''
            for j in range(15):
                if (self.grid[(i,j)].is_inhabited() == 0):
                    temp = "_"
                    line += temp.center(3, ' ')
                else:
                    line += self.grid[(i,j)].get_letter().center(3, ' ')
            print(line)
        return 0