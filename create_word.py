import pygame
pygame.init()
pygame.font.init() 
myfont = pygame.font.SysFont('kristenitc', 40)

class Word_button():
    displaystr = ''
    def __init__(self,surface,display_word):
        self.surface = surface
        self.display = display_word
        self.display_str = ''
        self.font =  'kristenitc'

    def create_word_button(self):
        button_1 = pygame.Rect(400,460,200,50)
        return button_1
        
    def draw_empty_word(self):
        
        for i in self.display:
            self.display_str += i
            self.display_str += ' '

        Word_button.displaystr = self.display_str
        textsurface = myfont.render(Word_button.displaystr, False, (0,0,0))
        self.surface.blit(textsurface,(400,350))
        return True