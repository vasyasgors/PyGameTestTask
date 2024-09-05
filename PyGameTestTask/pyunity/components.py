import pygame
import math


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

     def __init__(self):
        self.enabled = True

     def render(self, display):
        pass

     def get_rect(self): #уточнить, нужно ли
        pass

class SpriteRenderer(Renderer, pygame.sprite.Sprite):

    def __init__(self, path):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect(center=(0, 0))

    def render(self, display):
        if self.enabled == False:
            return

        display.blit(self.image, self.rect)

    def get_rect(self):
        return self.rect
    
class TextRenderer(Renderer):

    def __init__(self, font_path, size, color, text, position, multi_lines = False):
        super().__init__()
        self.font = pygame.font.Font(font_path, size)
        self.color = color
        self.text = text
        self.position = position
        self.rect = None
        self.size = size
        self.multi_lines = multi_lines


    def render(self, display):
        if self.enabled == False:
            return

        if self.multi_lines == True:
              self.blit_multi_lines_text(display, self.text, self.position, self.font, self.color)
        else:
            text_surface = self.font.render(self.text, True, self.color)
            self.rect = text_surface.get_rect()
            self.rect.center = (self.position.x, self.position.y)
            display.blit(text_surface, self.rect)
        
    # ВОЗМОЖНО И НЕ НУЖНО!
    def blit_multi_lines_text(self, surface, text, pos, font, color):
        words = [word.split(' ') for word in text.splitlines()] 
        space = font.size(' ')[0]
        max_width, max_height = surface.get_size()
        x = pos.x
        y = pos.y
        rects = []
        row_rects = []
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos.x
                    rects.append(row_rects)
                    row_rects = []
                row_rects.append(word)
                x += word_width + space
            x = pos.x
            rects.append(row_rects)
            row_rects = []

       
        max_vertical_rects = math.floor(max_height / font.size(' ')[1])
        printable_rects = rects[-max_vertical_rects:]
        for line in printable_rects:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos.x
            y += word_height


    def get_rect(self):
        return self.rect
