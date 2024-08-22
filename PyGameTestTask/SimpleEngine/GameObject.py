import pygame

class GameObject:

    def __init__(self, color, x, y, w, h):
        self.color = color
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def update(self):
       pass

    def render(self, display):
        pygame.draw.rect(display, self.color, (self.x, self.y, self.w, self.h))
        pass

