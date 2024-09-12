from behaviours import * 


game_time = 20
player_speed = 600

def create_main_scene():
    player_behaviour = PlayerBehaviour(player_speed)
    player_renderer = SpriteRenderer("Assets/Sprites/Ship.png")

    player_object = GameObject(player_behaviour, player_renderer, "Player")
    player_object.rect.x = 450
    player_object.rect.y = 480

    asteroid_spawner_behaviour = AsteroidSpawner(0.2,  Vector4(0, 800, -100, -90))
    asteroid_spawner_object = GameObject(asteroid_spawner_behaviour, None)

    score_render = TextRenderer(None, 50, (249, 223, 119), "-", Vector2(400, 40))
    score_object = GameObject(Score(score_render), score_render)

    game_timer_renderer = TextRenderer(None, 30, (249, 223, 119), "-", Vector2(400, 80))
    game_timer_behaviour = GameTimer(game_time, game_timer_renderer)
    game_timer_object = GameObject(game_timer_behaviour, game_timer_renderer)

    game_manager_behaviour = GameManager(score_object.behaviour, game_timer_behaviour, player_behaviour, asteroid_spawner_behaviour)
    game_manager_object = GameObject(game_manager_behaviour, None)

    task_lable_object = GameObject(None, TextRenderer(None, 20, (249, 223, 119), "Продержись заданное время и не врезайся в астероиды!", Vector2(400, 560)))
    hint_lable_object = GameObject(None, TextRenderer(None, 20, (249, 223, 119), "Пробел - стрелять, Двигаться - стрелки влево/вправо", Vector2(400, 580)))


    return Scene([player_object, 
                  asteroid_spawner_object, 
                  score_object, 
                  game_timer_object, 
                  game_manager_object,
                  task_lable_object,
                  hint_lable_object])
