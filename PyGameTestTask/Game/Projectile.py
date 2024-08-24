import pygame


from SimpleEngine.GameObject import * 
from SimpleEngine.Input import * 
from SimpleEngine.Game import * 

class Projectile(GameObject):
    
     def __init__(self, fileName, movementSpeed):
        super().__init__(fileName)
        self.movementSpeed = movementSpeed

     def update(self):
        self.rect.y -= self.movementSpeed * Time.DeltaTime
