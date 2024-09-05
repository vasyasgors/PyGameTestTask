class GameManager(Behaviour):

    instance = None

    def __init__(self, score, timer, player):
        super().__init__()
        GameManager.instance = self
        self.score = score
        self.timer = timer
        self.player = player
        self.state = GameState.PLAYING
        print_meow()
    
    def create_main_scene(self):
        player_behaviour = PlayerBehaviour(600)
        player_renderer = SpriteRenderer("Assets/Sprites/Ship.png")

        player_object = GameObject(player_behaviour, player_renderer, "Player")
        player_object.rect.x = 450
        player_object.rect.y = 480


        return Scene([player_object])

    def update(self):
         if Input.is_key_down(KeyCode.R):
            print("try to reload ")
            PyUnity.load_scene(self.create_main_scene())

    def on_player_collided_asteroid(self):
        self.state = GameState.DEFEAT
        lose_panel = GameObject(None, TextRenderer(None, 50, (249, 223, 119), "Проиграл", Vector2(400, 300)))
        PyUnity.add_object_to_loaded_scene(lose_panel)
        self.timer.enabled = False
        
    def on_projectile_collided_asteroid(self):
        self.score.add_score(1)
        self.score.update_score_text()
        pass

    def on_game_timer_finished(self):
        self.state = GameState.WIN
        self.timer.enabled = False
        self.player.enabled = False
        self.player.game_object.rect = None
        win_panel = GameObject(None, TextRenderer(None, 50, (249, 223, 119), "Победа", Vector2(400, 300)))
        PyUnity.add_object_to_loaded_scene(win_panel)
       
