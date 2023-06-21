
import pygame
# Va a representar cualquier objeto en un form - inclusive el propio form

class Widget():
    def __init__(self,screen,x,y,w,h,bg_color="Black",border_color="Red",border_size=-1):

        self._master = screen
        self._x = x
        self._y = y
        self._w = w
        self._h= h
        self._bg_color = bg_color
        self._border_color = border_color
        self.border_size = border_size
        self._slave = None
        self.slave_rect = None

    def update(self):
        pass

    def render(self):
        pass

    def draw(self):

        self._master.blit(self._slave, self.slave_rect)
        pygame.draw.rect(self._master, self._border_color, self.slave_rect, self.border_size)

    
