from pyunity.pyunity import *

from behaviours import *

#init game
PyUnity.create_display((800, 600), "TestTask", (39, 3, 58));


#create game object
player = GameObject(PlayerBehaviour(600), SpriteRenderer("Assets/Sprites/Ship.png"), "Player")
player.rect.x = 450
player.rect.y = 480



asteroid_spawner = GameObject(AsteroidSpawner(random.random(),  Vector4(0, 800, -100, -90)) )

score_text_render = TextRenderer(None, 50, (249, 223, 119), "0", Vector2(400, 40))
score_panel = GameObject(Score(score_text_render), score_text_render)


game_manager = GameObject( GameManager(score_panel.behaviour))



#create scene
main_scene = Scene([player, asteroid_spawner, score_panel]);
PyUnity.load_scene(main_scene)


