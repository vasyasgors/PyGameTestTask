import pygame
import copy
import random

from pyunity.components import * 
from pyunity.objects import * 
from pyunity.pyunity import * 


class GameManager(Behaviour):

    instance = None

    def __init__(self, score):
        self.score = score
        GameManager.instance = self


class Score(Behaviour):
    def __init__(self, text_render):
        self.score = 0
        self.text_render = text_render

    def add_score(self):
        self.score += 1
        self.text_render.text = str(self.score)


class PlayerBehaviour(Behaviour):
    
    def __init__(self, movement_speed):
       self.movement_speed = movement_speed
    
    def on_collied(self, other):
        if other.tag == "Asteroid":
            PyUnity.remove_object_form_loaded_scene(self.game_object)
            PyUnity.remove_object_form_loaded_scene(other)


    def update(self):
       if Input.is_key_pressed(KeyCode.LEFT_ARROW):
           self.game_object.rect.x -= self.movement_speed * Time.delta_time

       if Input.is_key_pressed(KeyCode.RIGHT_ARROW ):
           self.game_object.rect.x += self.movement_speed * Time.delta_time

       if Input.is_key_down(KeyCode.SPACE):
           projectile = GameObject( Projectile(-1, 1000, -100), SpriteRenderer("Assets/Sprites/Projectile.png"), "Projectile")
    
           projectile.rect.x = self.game_object.rect.x + self.game_object.rect.w / 2
           projectile.rect.y = self.game_object.rect.y - 20

           PyUnity.add_object_to_loaded_scene(projectile)



class Spawner(Behaviour):
    
     def __init__(self, spawn_rate, spawn_area):
        self.spawn_rate = spawn_rate
        self.spawn_area = spawn_area
        self.timer = 0
     
     def create_object(self, x, y):
        pass

     def update(self):
        self.timer += Time.delta_time

        if self.timer >= self.spawn_rate:
            x = random.randint(self.spawn_area.x, self.spawn_area.y)
            y = random.randint(self.spawn_area.z, self.spawn_area.w)

            self.create_object(x, y)
            self.timer = 0

class AsteroidSpawner(Spawner):
    def create_object(self, x, y):
        asteroid = GameObject( Mover(1, 400, 1000), SpriteRenderer("Assets/Sprites/Asteroid.png"), "Asteroid")
    
        asteroid.rect.x = x
        asteroid.rect.y = y

        PyUnity.add_object_to_loaded_scene(asteroid)


class Mover(Behaviour):

    #добавить destruction border
    def __init__(self, direction, speed, destory_y):
        self.direction = direction
        self.speed = speed
        self.destory_y = destory_y
    
    def update(self):
       self.game_object.rect.y += self.direction * self.speed * Time.delta_time

       if self.direction > 0:
           if self.game_object.rect.y >= self.destory_y:
               PyUnity.remove_object_form_loaded_scene(self.game_object)

       if self.direction <= 0:
           if self.game_object.rect.y <= self.destory_y:
               PyUnity.remove_object_form_loaded_scene(self.game_object)


class Projectile(Mover):


    def on_collied(self, other):       
 
        if other.tag == "Asteroid":
            GameManager.instance.score.add_score()
            PyUnity.remove_object_form_loaded_scene(self.game_object)
            PyUnity.remove_object_form_loaded_scene(other)