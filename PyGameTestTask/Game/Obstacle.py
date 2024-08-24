import pygame


from SimpleEngine.GameObject import * 
from SimpleEngine.Input import * 
from SimpleEngine.Game import * 

class Obstacle(GameObject):
    
     def __init__(self, color, x, y, w, h, movementSpeed):
        super().__init__(color, x, y, w, h)
        self.movementSpeed = movementSpeed

     def update(self):
        self.y += self.movementSpeed * Time.DeltaTime

        if self.y > 800:
            Game.Instance.RemoveGameObjectFromLoadedScene(self)
