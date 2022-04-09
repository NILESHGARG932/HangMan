
import pygame 
import random

from sympy import N
pygame.init()
screen = pygame.display.set_mode((600,500))
WHITE = (255, 255, 255)
image8 = pygame.image.load("sprites/img1.jpg")
image7 = pygame.image.load("sprites/img2.jpg")
image6 = pygame.image.load("sprites/img3.jpg")
image5 = pygame.image.load("sprites/img4.jpg")
image4 = pygame.image.load("sprites/img5.jpg")
image3 = pygame.image.load("sprites/img6.jpg")
image2 = pygame.image.load("sprites/img7.jpg")
image1 = pygame.image.load("sprites/img8.jpg")
image0 = pygame.image.load("sprites/img9.jpg")
images = [image0,image1,image2,image3,image4,image5,image6,image7,image8]

listofwords = ["absolute","abstract","academic","accepted","accurate","achieved","aircraft","baseball","bathroom"
"benjamin","commerce","ceiling","cleansing","dangerous","disaster","discover","divorce","elephant","elegant","etherum","flowchart",
"firewall","feedback","gorgeous","geometry","guidance","hardware","heritage","highland"
,"innocent","informal","interior","jungkook","jealous","joystick","keyboard","keystone","laughter","loneliness","loveliness","loudness"
,"management","million","mother","mammal","negative","nineteen","notebook","orange","obesity","olympiad","programming","python","parents",
 "question", "quantity","quality","robotics","rational","reliable","research","student","science","security","thirteen",
"thousand","tomorrow","ultimate","universe","umbrella","unicorn","venus","volcano","visionary","wildlife","wordpress","wikipedia",
"xbox","xenon","yourself","young","yatch","yellow","zebra","zipper"]
class Hangman():
    def __init__(self):
        self.noofmovesleft = 8
        self.guessletter = None
        self.image1 = pygame.image.load('sprites/img1.jpg')
        self.word = random.choice(listofwords).upper()
        self.displayword = ""
        for a in range(len(self.word)):
            self.displayword = self.displayword + "_ " 
        self.displaywordlist = list(self.displayword)   
        self.bigfont = pygame.font.SysFont('century',40,True)
        self.tfont = pygame.font.SysFont('century', 25, False)
        self.title = "HangMan Game"
        self.titlefont = self.bigfont.render(self.title,1,(0,0,0))
        self.wordfont = self.tfont.render(self.word, 1,(0,0,0))
        self.letterlist = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N",
        "O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        self.letterfontlist = []
        self.displaywordfont = self.tfont.render(self.displayword, 1, (0, 0, 0))
        x1 = 20
        y1 = 420
        for a in self.letterlist:
            if a == "N":
                x1 = 20
                y1 = 460
            self.letterfontlist.append([self.tfont.render(a,0,(0,0,0)),(x1,y1)])
            x1 = x1 + 30
            
    def gameplay(self,p):
        px = p[0]
        py = p[1]
        for a in self.letterfontlist:
            if (a[1][0]<=px and px < a[1][0]+30) and (a[1][1]<=py and py <= a[1][1] + a[0].get_height()):
                self.displaybox = False
                self.noofmovesleft = self.noofmovesleft - 1
                #print(self.noofmovesleft)
                self.letterindex = self.letterfontlist.index(a)
                self.guessletter = self.letterlist[self.letterindex]
                #print(self.guessletter)
                wordlen = len(self.word)
                
                for b in range(wordlen):  
                    if self.word[b] == self.guessletter:
                        self.displaywordlist[2*b] = self.guessletter
                        #print(self.displaywordlist)
                        #print(self.word)
                        self.displayword = ""
                        for s in self.displaywordlist:
                            self.displayword = self.displayword + s
                            self.displaywordfont = self.tfont.render(
                                self.displayword, 1, (0, 0, 0))
                        #self.letterfontlist.pop(self.letterindex)
                if self.guessletter in self.word:
                    self.noofmovesleft = self.noofmovesleft + 1
                    self.letterfontlist[self.letterindex][0] = self.tfont.render("_", 0, (0, 0, 0))

                i = 0
                while i < 500:
                    pygame.draw.rect(screen, (255,255,224), pygame.Rect(a[1][0], a[1][1], 25, 30))
                    screen.blit(a[0],a[1])
                    pygame.display.flip()
                    i= i+1
                         
                
        pass
    
    def display(self):
        screen.fill(WHITE)
        screen.blit(images[self.noofmovesleft],(100,200))
        screen.blit(self.titlefont, (300-self.titlefont.get_width()/2, 30))
        screen.blit(self.displaywordfont, (350,300))
        
        for a in self.letterfontlist:
            screen.blit(a[0],a[1])
        pygame.display.update()
        gotextfont = pygame.font.SysFont('century', 50, True)
        if self.noofmovesleft == 0:
            screen.fill(WHITE)
            pygame.display.update()
            gotext = "GAME OVER"
            
            gotextdis = gotextfont.render(gotext,0,(40,50,240))
            i = 0
            while i < 1000:
                screen.blit(gotextdis,(300-gotextdis.get_width()/2,200))
                pygame.display.update()
                i = i + 1
            pygame.quit()
            exit()
        self.matchword = self.displayword[::2]
        if self.matchword == self.word:
            screen.fill(WHITE)
            pygame.display.update()
            wintext = gotextfont.render("YOU WON ",0,(40,50,240))
            i = 0
            while i < 1000:
                screen.blit(wintext,(300-wintext.get_width()/2,200))
                pygame.display.update()
                i = i + 1
            pygame.quit()
            exit()
        pass
        

x = Hangman()
print(x.word)
print(x.letterfontlist)
while True:
    x.display()
    for event in pygame.event.get():
        
        if pygame.mouse.get_pressed() == (1,0,0):
            pos = pygame.mouse.get_pos()
            x.gameplay(pos)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            # 1,0,0 - left click

