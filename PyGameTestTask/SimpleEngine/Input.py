import pygame

class KeyCode:
    LeftArrow = pygame.K_LEFT
    RightArrow = pygame.K_RIGHT
    Space = pygame.K_SPACE

class Input:

    Keys = []
    Events = None

    @staticmethod
    def isKeyPressed(key):
        return Input.Keys[key];

    @staticmethod
    def isKeyDown(key):
        for event in Input.Events:
            if event.type == pygame.KEYDOWN and event.key == key:
                return True;
        return False