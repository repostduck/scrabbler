from Player import Player
from Letter import Letter
jeff = Player("Jeff")
jeff.updateScore(10)
print(jeff.getScore())
alpha = Letter('A')
jeff.addToHand(alpha)
print(alpha.getPoints())
z = jeff.getHand()
print(z[0].getPoints())
