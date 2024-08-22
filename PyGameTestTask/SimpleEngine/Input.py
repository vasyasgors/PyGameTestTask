import pygame

class KeyCode:
    LeftArrow = pygame.K_LEFT
    RightArrow = pygame.K_RIGHT

class Input:

    Keys = []

    @staticmethod
    def isKeyPressed(key):
        return Input.Keys[key];

