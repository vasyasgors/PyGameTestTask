import pygame

class Behaviour:

    def __init__(self):
        self.game_object = None

    def start(self):
        pass

    def update(self):
       pass

    def on_collied(self, other):
        pass

    def on_destroy(self):
        pass


class Renderer:
      def get_rect(self): #уточнить, нужно ли
        pass

class SpriteRenderer(pygame.sprite.Sprite, Renderer):

    def __init__(self, fileName):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(fileName).convert_alpha()
        self.rect = self.image.get_rect(center=(0, 0))

    def render(self, display):
        display.blit(self.image, self.rect)

    def get_rect(self):
        return self.rect

