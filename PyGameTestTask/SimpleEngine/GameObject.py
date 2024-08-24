import pygame

class GameObject(pygame.sprite.Sprite):

    def __init__(self, fileName):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(fileName).convert_alpha()
        self.rect = self.image.get_rect(center=(0, 0))

    def update(self):
       pass

    def render(self, display):
       #pygame.draw.rect(display, self.color, (self.x, self.y, self.w, self.h))
       display.blit(self.image, self.rect)
       pass

