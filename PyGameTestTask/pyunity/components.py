import pygame

class Behaviour:

    def __init__(self):
        self.game_object = None
        self.enabled = True

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

    def __init__(self, path):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect(center=(0, 0))

    def render(self, display):
        display.blit(self.image, self.rect)

    def get_rect(self):
        return self.rect
    
class TextRenderer(Renderer):

    def __init__(self, font_path, size, color, text, position):
        self.font = pygame.font.Font(font_path, size)
        self.color = color
        self.text = text
        self.position = position
        self.rect = None


    def render(self, display):
        text_surface = self.font.render(self.text, True, self.color)
        self.rect = text_surface.get_rect()
        self.rect.center = (self.position.x, self.position.y)

        display.blit(text_surface, self.rect)

    def get_rect(self):
        return self.rect
