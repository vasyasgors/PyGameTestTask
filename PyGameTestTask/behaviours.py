import copy
import random

from pyunity.components import * 
from pyunity.objects import * 
from pyunity.pyunity import * 

import config
import database

class GameManager(Behaviour):

    instance = None

    def __init__(self, score, timer, player, asteroid_spawner_behaviour):
        super().__init__()
        GameManager.instance = self

        self.score = score
        self.timer = timer
        self.player = player
        self.asteroid_spawner_behaviour = asteroid_spawner_behaviour

    def update(self):
         if Input.is_key_down(KeyCode.R):
             from scenes import create_main_scene
             PyUnity.load_scene(create_main_scene())

    def on_projectile_collided_asteroid(self):
        self.score.add_score(1)
        self.score.update_score_text()

    def on_player_collided_asteroid(self):
        PyUnity.add_object_to_loaded_scene(GameObject(None, TextRenderer(None, 50, (249, 223, 119), "Поражение", Vector2(400, 250))))
        PyUnity.add_object_to_loaded_scene(GameObject(None, TextRenderer(None, 20, (249, 223, 119), "Нажмите \"R\" - чтобы начать заново", Vector2(400, 280))))

        self.timer.enabled = False
        self.asteroid_spawner_behaviour.enabled = False

    def on_game_timer_finished(self):
        PyUnity.add_object_to_loaded_scene(GameObject(None, TextRenderer(None, 50, (249, 223, 119), "Победа", Vector2(400, 250))))
        PyUnity.add_object_to_loaded_scene(GameObject(None, TextRenderer(None, 20, (249, 223, 119), "Нажмите \"R\" - чтобы начать заново", Vector2(400, 280))))

        self.timer.enabled = False
        self.player.enabled = False
        self.player.game_object.rect = None
        self.asteroid_spawner_behaviour.enabled = False
        database.set_record(config.player_name, self.score.score)
        self.show_result()


    def show_result(self):
         record_list = database.get_records()
         color_other = (249, 223, 119)
         color_current = (200, 0, 0)
         color = color_other

         for i in range(len(record_list)):
              if record_list[i][0] == config.player_name: 
                  color = color_current
              else:
                  color = color_other
              dispaly_text = "Игрок: " + str(record_list[i][0]) + "   Очки: " + str(record_list[i][1])
              PyUnity.add_object_to_loaded_scene( GameObject(None, TextRenderer(None, 30, color, dispaly_text, Vector2(400, 340 + i * 20))) )

class Score(Behaviour):
    def __init__(self, text_render):
        super().__init__()
        self.score = 0
        self.text_render = text_render
        self.update_score_text()

    def add_score(self, value):
        self.score += value

    def update_score_text(self):
        self.text_render.text = "Очки " +  str(self.score)

class GameTimer(Behaviour):
    def __init__(self, time, text_render):
        super().__init__()
        self.time = time
        self.text_render = text_render

    def update(self):
        self.time -= Time.delta_time
        self.text_render.text = "Время "  + str(round(self.time, 1))

        if self.time <= 0:
            GameManager.instance.on_game_timer_finished()

        
class PlayerBehaviour(Behaviour):
    
    def __init__(self, movement_speed):
        super().__init__()
        self.movement_speed = movement_speed
    
    def on_collied(self, other):
        if other.tag == "Asteroid":
            GameManager.instance.on_player_collided_asteroid()

            PyUnity.remove_object_form_loaded_scene(self.game_object)
            PyUnity.remove_object_form_loaded_scene(other)


    def update(self):
       if Input.is_key_pressed(KeyCode.LEFT_ARROW) and self.game_object.rect.x > 0:
           self.game_object.rect.x -= self.movement_speed * Time.delta_time

       if Input.is_key_pressed(KeyCode.RIGHT_ARROW ) and self.game_object.rect.x < 800 - self.game_object.rect.w:
           self.game_object.rect.x += self.movement_speed * Time.delta_time

       if Input.is_key_down(KeyCode.SPACE):
           projectile = GameObject( Projectile(-1, 1000, -100), SpriteRenderer("Assets/Sprites/Projectile.png"), "Projectile")
    
           projectile.rect.x = self.game_object.rect.x + self.game_object.rect.w / 2
           projectile.rect.y = self.game_object.rect.y - 20

           PyUnity.add_object_to_loaded_scene(projectile)



class Spawner(Behaviour):
    
     def __init__(self, spawn_rate, spawn_area):
        super().__init__()
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

    def __init__(self, direction, speed, destory_y):
        super().__init__()
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
            GameManager.instance.on_projectile_collided_asteroid()
            PyUnity.remove_object_form_loaded_scene(self.game_object)
            PyUnity.remove_object_form_loaded_scene(other)