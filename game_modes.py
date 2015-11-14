import pygame
import constant
from utils import *

class GameMode(object):
	def __init__(self, screen):
		self.screen = screen

		self.background = create_tiled_surface(screen.get_size(), constant.BACKGROUND_PLAY)
		#self.background = pygame.image.load(constant.BACKGROUND_PLAY)
		self.screen.blit(self.background, (0, 0))

		self.game_over = False

	# 1 game chinh' gom` cac' buoc' sau
	def update(self):
		self.screen.blit(self.background, (0, 0))
		self.generate_game_items()
		self.handle_collisions()
		self.update_sprites()
		self.draw_changes()
		self.display_game_message()
		self.check_for_game_over()
		pygame.display.flip()

	def generate_game_items(self):
		raise Exception('Day la Abstract method, class con se~ override')
	def handle_collisions(self):
		raise Exception('Day la Abstract method, class con se~ override')
	def update_sprites(self):
		raise Exception('Day la Abstract method, class con se~ override')
	def draw_changes(self):
		raise Exception('Day la Abstract method, class con se~ override')
	def display_game_message(self):
		raise Exception('Day la Abstract method, class con se~ override')
	def check_for_game_over(self):
		raise Exception('Day la Abstract method, class con se~ override')
