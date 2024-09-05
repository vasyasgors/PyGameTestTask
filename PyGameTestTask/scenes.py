from behaviours import * 


def create_main_scene():
    player_behaviour = PlayerBehaviour(600)
    player_renderer = SpriteRenderer("Assets/Sprites/Ship.png")

    player_object = GameObject(player_behaviour, player_renderer, "Player")
    player_object.rect.x = 450
    player_object.rect.y = 480

    asteroid_spawner_behaviour = AsteroidSpawner(random.random(),  Vector4(0, 800, -100, -90))
    asteroid_spawner_object = GameObject(asteroid_spawner_behaviour, None)

    score_render = TextRenderer(None, 50, (249, 223, 119), "-", Vector2(400, 40))
    score_object = GameObject(Score(score_render), score_render)

    game_timer_renderer = TextRenderer(None, 30, (249, 223, 119), "-", Vector2(400, 80))
    game_timer_behaviour = GameTimer(1, game_timer_renderer)
    game_timer_object = GameObject(game_timer_behaviour, game_timer_renderer)

    game_manager_behaviour = GameManager(score_object.behaviour, game_timer_behaviour, player_behaviour)
    game_manager_object = GameObject(game_manager_behaviour, None)


    return Scene([player_object, 
                  asteroid_spawner_object, 
                  score_object, 
                  game_timer_object, 
                  game_manager_object ])
