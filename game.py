# game file

from menu import *
from tkinter import *
import pygame
import sys

# common variables that will be used for the menu system
class Game():
    def __init__(self):
        pygame.init()
        self.running = True
	self.playing = False
        self.keyUp = False
	self.keyDown = False
	self.keyStart = False
	self.keyBack = False
        self.displayWidth = 1100
	self.displayHeight = 650
        self.display = pygame.Surface((self.displayWidth,self.displayHeight))
        self.window = pygame.display.setMode(((self.displayWidth,self.displayHeight)))
        self.fontName = pygame.font.get_default_font()
        self.BLACK = (0, 0, 0)
	self.WHITE = (255, 255, 255)
        self.mainMenu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.currentMenu = self.mainMenu

    # the game loop itself
    def gameLoop(self):
        while self.playing:
            self.checkEvents()
            if self.keyStart:
                self.playing= False
            self.display.fill(self.BLACK)
            
            # initialize pygame ------------------------------
            pygame.init()

            # setup game window ------------------------------
            gameWindow = Tk()
            gameWindow.title("Who Wants to Be a CSC Master")    
            gameWindow.geometry('1100x650+0+0')
            gameWindow.configure(background='black')

            # setup all frames -------------------------------
            frame1 = Frame(gameWindow, bg='black', bd=20, width=900, height=600)
            frame1.grid(row=0, column=0)
            frame2 = Frame(gameWindow, bg='black', bd=20, width=452, height=600)
            frame2.grid(row=0, column=1)

            frame1a = Frame(frame1, bg='black', bd=20, width=900, height=200)
            frame1a.grid(row=0, column=0)
            frame1b = Frame(frame1, bg='black', bd=20, width=900, height=200)
            frame1b.grid(row=1, column=0)
            frame1c = Frame(frame1, bg='black', bd=20, width=900, height=200)
            frame1c.grid(row=2, column=0)

            # quit button ------------------------------------
            def closeGame():
                sys.exit()

            # advancing ladder -------------------------------
            def millionPic1():
                canvas = Canvas(frame2, bg='black', width=430, height=600)
                canvas.grid(row=0, column=0)
                canvas.delete("all")
                image1 = PhotoImage(file = 'pic1.png')
                canvas.create_image(215, 300, image=image1)
                canvas.image = image1

            def millionPic2():
                canvas = Canvas(frame2, bg='black', width=430, height=600)
                canvas.grid(row=0, column=0)
                canvas.delete("all")
                image1 = PhotoImage(file = 'pic2.png')
                canvas.create_image(215, 300, image=image1)
                canvas.image = image1

            def millionPic3():
                canvas = Canvas(frame2, bg='black', width=430, height=600)
                canvas.grid(row=0, column=0)
                canvas.delete("all")
                image1 = PhotoImage(file = 'pic3.png')
                canvas.create_image(215, 300, image=image1)
                canvas.image = image1

            def millionPic4():
                canvas = Canvas(frame2, bg='black', width=430, height=600)
                canvas.grid(row=0, column=0)
                canvas.delete("all")
                image1 = PhotoImage(file = 'pic4.png')
                canvas.create_image(215, 300, image=image1)
                canvas.image = image1

            def millionPic5():
                canvas = Canvas(frame2, bg='black', width=430, height=600)
                canvas.grid(row=0, column=0)
                canvas.delete("all")
                image1 = PhotoImage(file = 'pic5.png')
                canvas.create_image(215, 300, image=image1)
                canvas.image = image1

            def millionPic6():
                canvas = Canvas(frame2, bg='black', width=430, height=600)
                canvas.grid(row=0, column=0)
                canvas.delete("all")
                image1 = PhotoImage(file = 'pic6.png')
                canvas.create_image(215, 300, image=image1)
                canvas.image = image1

            def millionPic7():
                canvas = Canvas(frame2, bg='black', width=430, height=600)
                canvas.grid(row=0, column=0)
                canvas.delete("all")
                image1 = PhotoImage(file = 'pic7.png')
                canvas.create_image(215, 300, image=image1)
                canvas.image = image1

            def millionPic8():
                canvas = Canvas(frame2, bg='black', width=430, height=600)
                canvas.grid(row=0, column=0)
                canvas.delete("all")
                image1 = PhotoImage(file = 'pic8.png')
                canvas.create_image(215, 300, image=image1)
                canvas.image = image1

            def millionPic9():
                canvas = Canvas(frame2, bg='black', width=430, height=600)
                canvas.grid(row=0, column=0)
                canvas.delete("all")
                image1 = PhotoImage(file = 'pic9.png')
                canvas.create_image(215, 300, image=image1)
                canvas.image = image1

            def millionPic10():
                canvas = Canvas(frame2, bg='black', width=430, height=600)
                canvas.grid(row=0, column=0)
                canvas.delete("all")
                image1 = PhotoImage(file = 'pic10.png')
                canvas.create_image(215, 300, image=image1)
                canvas.image = image1

            def millionPic11():
                canvas = Canvas(frame2, bg='black', width=430, height=600)
                canvas.grid(row=0, column=0)
                canvas.delete("all")
                image1 = PhotoImage(file = 'pic11.png')
                canvas.create_image(215, 300, image=image1)
                canvas.image = image1

            def millionPic12():
                canvas = Canvas(frame2, bg='black', width=430, height=600)
                canvas.grid(row=0, column=0)
                canvas.delete("all")
                image1 = PhotoImage(file = 'pic12.png')
                canvas.create_image(215, 300, image=image1)
                canvas.image = image1

            def millionPic13():
                canvas = Canvas(frame2, bg='black', width=430, height=600)
                canvas.grid(row=0, column=0)
                canvas.delete("all")
                image1 = PhotoImage(file = 'pic13.png')
                canvas.create_image(215, 300, image=image1)
                canvas.image = image1

            def millionPic14():
                canvas = Canvas(frame2, bg='black', width=430, height=600)
                canvas.grid(row=0, column=0)
                canvas.delete("all")
                image1 = PhotoImage(file = 'pic14.png')
                canvas.create_image(215, 300, image=image1)
                canvas.image = image1

            def millionPic15():
                canvas = Canvas(frame2, bg='black', width=430, height=600)
                canvas.grid(row=0, column=0)
                canvas.delete("all")
                image1 = PhotoImage(file = 'pic15.png')
                canvas.create_image(215, 300, image=image1)
                canvas.image = image1
            
            # load initial images ----------------------------
            CentreImage = PhotoImage(file = 'Centre.png')
            LogoCentre = Button(frame1b, image = CentreImage, bg='black', width=300, height=200)
            LogoCentre.grid()

            ImageQuit = PhotoImage(file = 'quitButton.png')
            LiveQuit = Button(frame1a, image = ImageQuit, bg='black', width=150, height=70, command = closeGame)
            LiveQuit.grid(row=0, column=0)

            ImageMillion00 = PhotoImage(file = 'million00.png')
            LiveMillion00 = Button(frame2, image = ImageMillion00, bg='black', width=430, height=600)
            LiveMillion00.grid(row=0, column=0)

            # questions --------------------------------------
            question1 = StringVar()
            question2 = StringVar()
            question3 = StringVar()
            question4 = StringVar()
            question5 = StringVar()
            question6 = StringVar()
            question7 = StringVar()
            question8 = StringVar()
            question9 = StringVar()
            question10 = StringVar()
            question11 = StringVar()
            question12 = StringVar()
            question13 = StringVar()
            question14 = StringVar()
            question15 = StringVar()

            answer1 = StringVar()
            answer2 = StringVar()
            answer3 = StringVar()
            answer4 = StringVar()

            question1.set("What is the value of 17 % 7?")
            answer1.set("1")
            answer2.set("2")
            answer3.set("4") 
            answer4.set("3") # correct ans

            def question2():
                question2.set("Which is a legal identifier?")
                answer1.set("program_1") # correct ans
                answer2.set("program!") 
                answer3.set("1program")
                answer4.set("program 1")
                millionPic1()

            def question3():
                question3.set("Which is the 'brain' of a computer?")
                answer1.set("MM")
                answer2.set("ROM")
                answer3.set("CPU") # correct ans
                answer4.set("RAM") 
                millionPic2()

            def question4():
                question4.set("Which is a relational operator?")
                answer1.set("=") 
                answer2.set("==") # correct ans
                answer3.set("!")
                answer4.set("&&")
                millionPic3()

            def question5():
                question5.set("Next Fiboncci number? 1,1,2,3,5,[]")
                answer1.set("7") 
                answer2.set("8") # correct ans
                answer3.set("6") 
                answer4.set("9")
                millionPic4()
            
            # text, labels, buttons --------------------------
            txtQuestion = Entry(frame1c, font=('arial', 18, 'bold'), bg='blue', fg='white', bd=5, width=44,
                                justify=CENTER, textvariable = question1)
            txtQuestion.grid(row=0, column=0, columnspan=4, pady=4)

            lblQuestionA = Label(frame1c, font=('arial', 14, 'bold'), text='A: ', bg='black', fg='white', bd=5, justify=CENTER)
            lblQuestionA.grid(row=1, column=0, pady=4, sticky=W)
            txtQuestionA = Button(frame1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=5, width=17, height=2,
                                  justify=CENTER, textvariable = answer1, command=question3)
            txtQuestionA.grid(row=1, column=1, pady=4)

            lblQuestionB = Label(frame1c, font=('arial', 14, 'bold'), text='B: ', bg='black', fg='white', justify=LEFT)
            lblQuestionB.grid(row=1, column=2, sticky=W)
            txtQuestion2 = Button(frame1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=5, width=17, height=2,
                                  justify=CENTER, textvariable = answer2, command=question5)
            txtQuestion2.grid(row=1, column=3, pady=4)

            lblQuestionC = Label(frame1c, font=('arial', 14, 'bold'), text='C: ', bg='black', fg='white', justify=LEFT)
            lblQuestionC.grid(row=2, column=0, sticky=W)
            txtQuestion3 = Button(frame1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=5, width=17, height=2,
                                  justify=CENTER, textvariable = answer3, command=question4)
            txtQuestion3.grid(row=2, column=1, pady=4)

            lblQuestionD = Label(frame1c, font=('arial', 14, 'bold'), text='D: ', bg='black', fg='white', justify=LEFT)
            lblQuestionD.grid(row=2, column=2, sticky=W)
            txtQuestion4 = Button(frame1c, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=5, width=17, height=2,
                                  justify=CENTER, textvariable = answer4, command=question2)
            txtQuestion4.grid(row=2, column=3, pady=4)

            gameWindow.mainloop()
            pygame.quit()
            
            self.window.blit(self.display, (0,0))
            pygame.display.update()
            self.resetKeys()

    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
		self.playing = False
                self.currentMenu.runDisplay = False
            if event.type == pygame.keyDown:
                if event.key == pygame.K_RETURN:
                    self.keyStart = True
                if event.key == pygame.K_BACKSPACE:
                    self.keyBack = True
                if event.key == pygame.K_DOWN:
                    self.keyDown = True
                if event.key == pygame.K_UP:
                    self.keyUp = True

    def resetKeys(self):
        self.keyUp = False
	self.keyDown = False
	self.keyStart = False
	self.keyBack = False

    def drawText(self, text, size, x, y ):
        font = pygame.font.Font(self.fontName,size)
        textSurface = font.render(text, True, self.WHITE)
        textRectangle = textSurface.getRectangle()
        textRectangle.center = (x,y)
        self.display.blit(textSurface,textRectangle)
