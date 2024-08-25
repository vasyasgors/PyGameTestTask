import pygame
import random

from SimpleEngine.GameObject import * 
from SimpleEngine.Input import * 
from SimpleEngine.Game import *
from Game.Obstacle import *



class Spawner(GameObject):
    
     def __init__(self, spawnRate, spawnWidth):
        self.spawnRate = spawnRate
        self.spawnWidth = spawnWidth
        self.timer = 0

     def update(self):
         self.timer += Time.DeltaTime

         if self.timer >= self.spawnRate:
            obstacle = Obstacle("Assets/Sprites/Asteroid.png", random.randint(100, 200))
            obstacle.rect.x = random.randint(0, self.spawnWidth)
            obstacle.rect.y = -100
            Game.Instance.AddGameObjectToLoadedScene(obstacle);
            self.timer = 0
         pass
