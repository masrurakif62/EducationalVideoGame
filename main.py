#main file

from game import Game

g = Game()

while g.running:
    g.currentMenu.displayMenu()
    g.gameLoop()

