import pygame
import sys

from SimpleEngine.GameObject import * 
from SimpleEngine.Input import * 
from SimpleEngine.Scene import * 
from SimpleEngine.Time import * 

class Game:


	def __init__(self, backgroundColor, targetFPS):
		self.backgroundColor = backgroundColor
		self.targetFPS = targetFPS

	def InitDisplay(self, size, title):
		pygame.init()

		self.display = pygame.display.set_mode(size)
		pygame.display.set_caption(title)
		
		self.clock = pygame.time.Clock()
		

	def Start(self, scene):
		self.scene = scene
		self.started = True

		while self.started == True:
			self.display.fill(self.backgroundColor)

			events = pygame.event.get()

			Input.Keys = pygame.key.get_pressed()

			for event in events:
				if event.type == pygame.QUIT:
					pygame.quit()
					return

			scene.update()

			self.scene.render(self.display)
			pygame.display.update()

			Time.DeltaTime = self.clock.tick(self.targetFPS) / 1000
