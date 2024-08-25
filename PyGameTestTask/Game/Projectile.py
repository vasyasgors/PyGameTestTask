import pygame


from SimpleEngine.GameObject import * 
from SimpleEngine.Input import * 
from SimpleEngine.Game import * 

#Сделать один мовабле
class Projectile(SpriteGameObject):
    
     def __init__(self, fileName, movementSpeed):
        super().__init__(fileName)
        self.movementSpeed = movementSpeed

     def update(self):
        self.rect.y -= self.movementSpeed * Time.DeltaTime

        if self.rect.y < -100:
            Game.Instance.RemoveGameObjectFromLoadedScene(self)
