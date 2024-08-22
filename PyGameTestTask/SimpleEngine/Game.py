import pygame
import sys

from SimpleEngine.GameObject import * 
from SimpleEngine.Input import * 
from SimpleEngine.Scene import * 
from SimpleEngine.Time import * 

class Game:

	Instance = None

	def __init__(self, backgroundColor, targetFPS):
		self.backgroundColor = backgroundColor
		self.targetFPS = targetFPS
		Game.Instance = self;

	def InitDisplay(self, size, title):
		pygame.init()

		self.display = pygame.display.set_mode(size)
		pygame.display.set_caption(title)
		
		self.clock = pygame.time.Clock()
		

	def Start(self, scene):
		self.loadedScene = scene
		self.started = True

		while self.started == True:
			self.display.fill(self.backgroundColor)

			Input.Events = pygame.event.get()

			Input.Keys = pygame.key.get_pressed()

			for event in Input.Events:
				if event.type == pygame.QUIT:
					pygame.quit()
					return

			self.loadedScene.update()

			self.loadedScene.render(self.display)
			pygame.display.update()

			Time.DeltaTime = self.clock.tick(self.targetFPS) / 1000

	def LoadScene(self, scene):
		self.loadedScene = scene

	def SpawnGameObject(self, object):
		if self.loadedScene != None:
			self.loadedScene.objects.append(object);
		
	def DestroyGameObject(self, object):
		self.loadedScene.objects.remove(object);
		
		
