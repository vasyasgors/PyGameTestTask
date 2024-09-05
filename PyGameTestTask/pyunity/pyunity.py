import pygame
import sys

from .components import *
from .objects import *
from .scene import *
from .input import *

class Time:
	delta_time = 0

class PyUnity:

	TARGET_FPS = 60

	display = None
	background_color = None
	loaded_scene = None
	is_started = False
	clock = None
	
	@staticmethod
	def create_display(size, title, background_color):
		PyUnity.background_color = background_color
		
		pygame.init()
		PyUnity.display = pygame.display.set_mode(size)
		pygame.display.set_caption(title)
		PyUnity.clock = pygame.time.Clock()
		
	@staticmethod
	def start_main_loop(scene):
		PyUnity.loaded_scene = scene
		PyUnity.is_started = True

		while PyUnity.is_started == True:
			PyUnity.display.fill(PyUnity.background_color)

			Input.events = pygame.event.get()

			Input.keys = pygame.key.get_pressed()

			for event in Input.events:
				if event.type == pygame.QUIT:
					pygame.quit()
					return

			PyUnity.loaded_scene.update()

			PyUnity.loaded_scene.render(PyUnity.display)
			pygame.display.update()

			Time.delta_time = PyUnity.clock.tick(PyUnity.TARGET_FPS) / 1000
		
	@staticmethod	
	def add_object_to_loaded_scene(object):
		if PyUnity.loaded_scene != None:
			PyUnity.loaded_scene.add_object(object);

	@staticmethod	
	def remove_object_form_loaded_scene(object):
		if PyUnity.loaded_scene != None:
			PyUnity.loaded_scene.remove_object(object);

	@staticmethod	
	def load_scene(scene):
		PyUnity.loaded_scene = scene
