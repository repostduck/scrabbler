from Letter import Letter


class Tile:
    def __init__ (self):
        self.letter = None
        self.bonus = 'Normal'

    def modBonus(self, value):
        if value is not ('Normal' or 'Letter_3' or 'Word_3' or 'Letter_2' or 'Word_2'):
            raise ValueError("inappropriate bonus value phrase")
        else:
            self.bonus = value
        return
    def getBonus(self, value):
        return self.bonus

#initialize a grid of 15 x 15 tiles and assign values to each
#parameter: bonusCoords is a list acting as a stack containing (x,y) values
class Board:
    def __init__ (self, game, bonusCoords):
        self.grid = dict()
        for x in range(15):
            for y in range(15):
                self.grid[(x,y)] = Tile()
        self.game = game
    def __updateTile__ (self, coord, letter):
        #assign the Letter to the designated tile
        #return calculated (2l, 3l) score and type of multiplier (normal, 2w, 3w)
        #removes existing bonus if any
        #TODO
        pass
