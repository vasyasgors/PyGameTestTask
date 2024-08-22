from SimpleEngine.Game import * 
from Game.Player import * 

player = Player((255, 255, 255), x = 400, y = 530, w = 50, h = 50, movementSpeed = 10)

scene = Scene([player]);

game = Game((0, 0, 0), 60)
game.InitDisplay((800, 600), "TestTask")
game.Start(scene)


