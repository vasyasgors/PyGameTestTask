import pygame


from SimpleEngine.GameObject import * 
from SimpleEngine.Input import * 
from SimpleEngine.Game import * 

from Game.Projectile import * 

class Player(GameObject):
    
     def __init__(self, color, x, y, w, h, movementSpeed):
        super().__init__(color, x, y, w, h)
        self.movementSpeed = movementSpeed

     def update(self):
        if Input.isKeyPressed(KeyCode.LeftArrow):
            self.x -= 10

        if Input.isKeyPressed(KeyCode.RightArrow):
            self.x += 10

        if Input.isKeyDown(KeyCode.Space):
            Game.Instance.SpawnGameObject(Projectile((255, 255, 255), x = self.x, y = self.y, w = 10, h = 10, movementSpeed = 500));
