from pyunity.pyunity import *

from behaviours import *

#init game
PyUnity.create_display((800, 600), "TestTask", (39, 3, 58));


#create game object
player = GameObject( PlayerBehaviour(400), SpriteRenderer("Assets/Sprites/Ship.png"), "Player")
player.rect.x = 450
player.rect.y = 400





#create scene
main_scene = Scene([player]);
PyUnity.load_scene(main_scene)


