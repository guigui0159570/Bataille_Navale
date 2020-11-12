import pygame
from pygame.locals import*

noir = (0, 0, 0)

class Boutons():
    def __init__(self, color, x,y,width,height, text='', colortext=noir):
        """
        Méthode constructeur qui créer le bouton.
        """
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.colortext = colortext

    def draw(self,win,outline=None):
        """
        Méthode qui dessine le bouton.
        """
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, self.colortext)
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        """
        Méthode qui renvoie True ou False si on clique dessus.
        """
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False
