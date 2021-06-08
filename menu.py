# menu file

import pygame

class Menu():
    def __init__(self, game):
        self.game = game
        self.middleWidth = self.game.displayWidth / 2
	self.middleHeight = self.game.displayHeight / 2
        self.runDisplay = True
        self.cursorRectangle = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def drawCursor(self):
        self.game.drawText('*', 15, self.cursorRectangle.x, self.cursorRectangle.y)

    def blitScreen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.resetKeys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startX = self.middleWidth
	self.startY = self.middleHeight + 30
        self.optionsX = self.middleWidth
	self.optionsY = self.middleHeight + 50
        self.creditsX = self.middleWidth
	self.creditsy = self.middleHeight + 70
        self.cursorRectangle.midtop = (self.startX + self.offset, self.startY)

    def displayMenu(self):
        self.runDisplay = True
        while self.runDisplay:
            self.game.checkEvents()
            self.checkInput()
            self.game.display.fill(self.game.BLACK)
            self.game.drawText('Who Wants to Be a CSC Master', 20, self.game.displayWidth / 2, self.game.displayHeight / 2 - 20)
            self.game.drawText("Start Game", 20, self.startX, self.startY)
            self.game.drawText("Options", 20, self.optionsX, self.optionsY)
            self.game.drawText("Credits", 20, self.creditsX, self.creditsY)
            self.drawCursor()
            self.blitScreen()


    def moveCursor(self):
        if self.game.keyDown:
            if self.state == 'Start':
                self.cursorRectangleect.midtop = (self.optionsX + self.offset, self.optionsY)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursorRectangle.midtop = (self.creditsX + self.offset, self.creditsY)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursorRectangle.midtop = (self.startX + self.offset, self.startY)
                self.state = 'Start'
        elif self.game.keyUp:
            if self.state == 'Start':
                self.cursorRectangle.midtop = (self.creditsX + self.offset, self.creditsY)
                self.state = 'Credits'
            elif self.state == 'Options':
                self.cursorRectangle.midtop = (self.startX + self.offset, self.startY)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursorRectangle.midtop = (self.optionsX + self.offset, self.optionsY)
                self.state = 'Options'

    def checkInput(self):
        self.moveCursor()
        if self.game.keyStart:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                self.game.currentMenu = self.game.options
            elif self.state == 'Credits':
                self.game.currentMenu = self.game.credits
            self.run_display = False

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volumeX = self.middleWidth
	self.volumeY = self.middleHeight + 20
        self.controlsX = self.middleWidth
	self.controlsy = self.middleHeight + 40
        self.cursorRectangle.midtop = (self.volumeX + self.offset, self.volumeY)

    def displayMenu(self):
        self.runDisplay = True
        while self.runDisplay:
            self.game.checkEvents()
            self.checkInput()
            self.game.display.fill((0, 0, 0))
            self.game.drawText('Options', 20, self.game.displayWidth / 2, self.game.displayHeight / 2 - 30)
            self.game.drawText("Volume", 15, self.volumeX, self.volumeY)
            self.game.drawText("Controls", 15, self.controlsX, self.controlsY)
            self.drawCursor()
            self.blitScreen()

    def checkInput(self):
        if self.game.keyBack:
            self.game.currentMenu = self.game.mainMenu
            self.runDisplay = False
        elif self.game.keyUp or self.game.keyDown:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursorRectangle.midtop = (self.controlsX + self.offset, self.controlsY)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursorRectangle.midtop = (self.volumeX + self.offset, self.volumeY)
        elif self.game.keyStart:
            # Masrur's note: would have added volume and controls functions here
            pass

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def displayMenu(self):
        self.runDisplay = True
        while self.runDisplay:
            self.game.checkEvents()
            if self.game.keyStart or self.game.keyBack:
                self.game.currentMenu = self.game.mainMenu
                self.runDisplay = False
            self.game.display.fill(self.game.BLACK)
            self.game.drawText('Credits', 20, self.game.displayWidth / 2, self.game.displayHeight / 2 - 20)
            self.game.drawText('Made by Masrur Akif', 15, self.game.displayWidth / 2, self.game.displayHeight / 2 + 10)
            self.blitScreen()
