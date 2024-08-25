import pygame


from SimpleEngine.GameObject import * 
from SimpleEngine.Input import * 
from SimpleEngine.Game import * 

from Game.Projectile import * 

class Player(SpriteGameObject):
    
     def __init__(self, fileName, movementSpeed):
        super().__init__(fileName)
        self.movementSpeed = movementSpeed

     def update(self):
        if Input.isKeyPressed(KeyCode.LeftArrow):
            self.rect.x -= self.movementSpeed * Time.DeltaTime

        if Input.isKeyPressed(KeyCode.RightArrow):
             self.rect.x += self.movementSpeed * Time.DeltaTime

        if Input.isKeyDown(KeyCode.Space):
            projectile = Projectile("Assets/Sprites/Projectile.png", 1000)
            projectile.rect.x = self.rect.x + self.rect.w / 2
            projectile.rect.y = self.rect.y - 20
            Game.Instance.AddGameObjectToLoadedScene(projectile);
