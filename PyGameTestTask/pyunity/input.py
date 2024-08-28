import pygame

class KeyCode:
    LEFT_ARROW = pygame.K_LEFT
    RIGHT_ARROW = pygame.K_RIGHT
    SPACE = pygame.K_SPACE

class Input:

    keys = []
    events = None

    @staticmethod
    def is_key_pressed(key):
        return Input.keys[key];

    @staticmethod
    def is_key_down(key):
        for event in Input.events:
            if event.type == pygame.KEYDOWN and event.key == key:
                return True;
        return False