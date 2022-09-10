import pygame
import ptext12 as ptext
import random
from create_word import Word_button

mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('hangman')
screen = pygame.display.set_mode((1000,600),0,32)
clicking = False
drawn = False
chosen_word = ''
font = pygame.font.Font(None, 32)
with open('words_to_use.txt','r') as f:
    mylist = [line.rstrip() for line in f]
    chosen_word = random.choice(mylist)
text = ''
pygame.font.init() 
myfont = pygame.font.SysFont('kristenitc', 40)
myfont1 = pygame.font.SysFont('kristenitc', 25)
myfont2 = pygame.font.SysFont('kristenitc', 20)
lives = 10
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += '_'
letter_set = set(chosen_word)

class Button:

    def __init__(self,surface, color, x, y, radius, text,display_word):
        self.surface = surface
        self.radius = radius
        self.color = color
        self.x = x
        self.y = y
        self.width = 40
        self.text = text
        self.visible = True
        self.height = 40
        self.font =  'kristenitc'
        self.fontsize = 20
        self.tcolor = (0,0,0)
        self.display = display_word
        self.btn = pygame.Rect(self.x,self.y,self.width,self.height)

    def draw(self):
        self.btn1 = pygame.draw.rect(self.surface,self.color,self.btn,border_radius=self.radius)
        ptext.draw(self.text,center=self.btn.center,color=self.tcolor,sysfontname=self.font,fontsize=self.fontsize)

    def hover(self, pos):
        if self.btn.collidepoint(pos):
            self.color = (0,0,0)
            return True
        return False

    def return_display(self):
        textsurface1 = myfont.render(f'{self.text}', False, (0,0,0))
        self.surface.blit(textsurface1,(170,150))
        letter_click = self.text
        for index,letter in enumerate(chosen_word):
           if letter == letter_click:
              self.display[index] = letter


    def comparison_word2(self):
         textsurface1 = myfont.render(f'{self.text}', False, (0,0,0))
         self.surface.blit(textsurface1,(170,150))
         letter_clicks = self.text
         if letter_clicks not in [*chosen_word]:
             return False

posX = 220
posY = 35
posY1 = 90
posX1 = 220
posX2 = 220
posY2 = 145
posX3 = 220
posY3 = 200
letter_btnH = 40
letter_btnW = 40
color = 'lightskyblue3'



victory = False
defeat = False
run = True
letters = []
comparison_letters = {}
used_letters = set()

def redraw_screen():
    screen.fill((255, 255, 255))
    for letter in comparison_letters.values():
        letter.draw()

while run:
        redraw_screen()
        mainClock.tick(60)
        mx,my = pygame.mouse.get_pos()

        alphabet = list("abcdefghijklmnopqrstuvwxyz")
        x1, y1 = 135, 35
        x2, y2 = 135, 90
        count1 = 0
        count2 = 13
        for i in range(13):
            letter_1 = Button(screen,'lightskyblue3', x1, y1, 25, alphabet[i],display)
            comparison_letters[str(count1)] = letter_1
            x1 += 60
            count1 += 1
        for i in range(13, 26):
            letter_2 = Button(screen,'lightskyblue3', x2, y2, 25, alphabet[i],display)
            comparison_letters[str(count2)] = letter_2
            x2 += 60
            count2 += 1

        button_set = Word_button(screen,display)
        button_set_1 = button_set.create_word_button()
        if button_set_1.collidepoint((mx,my)):
           if clicking:
              pygame.display.update()
              drawn = True
        if drawn:
           button_set.draw_empty_word()              
        
        pygame.draw.rect(screen, (255,0,0), button_set_1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


            elif event.type == pygame.MOUSEBUTTONDOWN:
                clicking = True
                for letter in comparison_letters.values():
                    if letter.hover(pygame.mouse.get_pos()):
                      if drawn:
                       if letter.text not in used_letters:
                           used_letters.add(letter.text)
                           letter.return_display()
                           if letter.comparison_word2() == False:
                                lives -= 1
   

            elif event.type == pygame.MOUSEBUTTONUP:
                clicking = False

        for letter in comparison_letters.values():
            if letter.text in used_letters:
                letter.color = (220,220,220)

        livesCounter = myfont1.render(f'Lives:{lives}', False, (0,0,0))
        screen.blit(livesCounter,(30,60))
        RedButtonTeller = myfont2.render(f'This red button chooses a word randomly', False, (0,0,0))
        screen.blit(RedButtonTeller,(280,530))
        if lives == 0:
           clicking = False
           drawn = False
           victory = True
           defeat_text = myfont.render('You lose', False, (0,0,0))
           screen.blit(defeat_text,(430,300))
           lives = 10
           display = []
           used_letters = set()
           displaystrs = ''
           with open('words_to_use.txt','r') as f:
                 mylist = [line.rstrip() for line in f]
                 chosen_word = random.choice(mylist)
           word_length = len(chosen_word)
           for _ in range(word_length):
                 display += '_'
           pygame.display.update()

        
        elif display == [*chosen_word]:
           clicking = False
           drawn = False
           victory = True
           victory_text = myfont.render('You win', False, (0,0,0))
           screen.blit(victory_text,(430,300))
           lives = 10
           display = []
           used_letters = set()
           displaystrs = ''
           with open('words_to_use.txt','r') as f:
                 mylist = [line.rstrip() for line in f]
                 chosen_word = random.choice(mylist)
           word_length = len(chosen_word)
           for _ in range(word_length):
                 display += '_'
           pygame.display.update()
 
        pygame.display.update()
quit()