import pygame


from pyunity.components import * 
from pyunity.objects import * 
from pyunity.pyunity import * 

class PlayerBehaviour(Behaviour):
    
     def __init__(self, movement_speed):
        self.movement_speed = movement_speed

     def update(self):
        if Input.is_key_pressed(KeyCode.LEFT_ARROW):
            self.game_object.rect.x -= self.movement_speed * Time.delta_time

        if Input.is_key_pressed(KeyCode.RIGHT_ARROW ):
            self.game_object.rect.x += self.movement_speed * Time.delta_time

        if Input.is_key_down(KeyCode.SPACE):
            projectile = GameObject( Mover(1, -1000), SpriteRenderer("Assets/Sprites/Projectile.png"))
    
            projectile.rect.x = self.game_object.rect.x + self.game_object.rect.w / 2
            projectile.rect.y = self.game_object.rect.y - 20

            PyUnity.add_object_to_loaded_scene(projectile)


class Mover(Behaviour):

    #добавить destruction border
    def __init__(self, direction, speed):
        self.direction = direction
        self.speed = speed
    
    def update(self):
       self.game_object.rect.y += self.direction * self.speed * Time.delta_time