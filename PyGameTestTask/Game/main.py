from SimpleEngine.Game import * 
from Game.Player import * 

game = Game((39, 3, 58), 60)
game.InitDisplay((800, 600), "TestTask")

player = Player("Assets/Sprites/Ship.png", 1000)
player.rect.x = 400
player.rect.y = 500

scene = Scene([player]);
game.Start(scene)


