import pygame
import random
import constant
import game_items

class Enemy(pygame.sprite.Sprite):
	def __init__(self, game):
		pygame.sprite.Sprite.__init__(self)
		self.game = game
		self.screen = self.game.screen
		# hinh, toa do xuat hien, mau
		self.image = pygame.image.load(constant.ENEMY_IMAGE)
		self.rect = self.image.get_rect()
		self.rect.centerx = random.randint(0, self.screen.get_width())
		self.rect.centery = random.randint(0, self.screen.get_height())
		self.hp = constant.ENEMY_HP

		# move cua moi~ enemy la ngau nhien
		self.x = random.randint(constant.ENEMY_SPEED_MIN, constant.ENEMY_SPEED_MAX)
		self.y = random.randint(constant.ENEMY_SPEED_MIN, constant.ENEMY_SPEED_MAX)

		# thoi gian ban' ra cung ngau nhien
		self.shootcounter = random.randint(constant.ENEMY_MIN_BULLET_SPEED, constant.ENEMY_MAX_BULLET_SPEED)

		# sprite group dan. cua? dich
		self.bullets_sprite_list = pygame.sprite.Group()

		self.directions = ('n', 'e', 's', 'w', 'nw', 'ne', 'sw', 'se')

	# check enemy ko duoc vuot qua man hinh 
	# tu dong di chuyen enemy, doi huong' khi va cham 
	# tu. dong ban' dan.
	def update(self):
		"""
		Allows a game to update this sprite.
		"""
		self.boundaries()
		self.move()
		self.shootcounter -= 1
		if self.shootcounter == 0:
			# neu het thoi gian thi enemy duoc phep ban' , ban ngau nhien 1 trong 8 huong 
			self.shoot(self.directions[random.randint(0, 7)])
			self.shootcounter = random.randint(50, 100)

	def boundaries(self):
		"""
		Ensures that when this sprite hits the edge of the screen, it bounces off again and stays in the game.
		"""
		if self.rect.x <= 0:
			self.rect.x = 0
		if self.rect.x >= (self.screen.get_width() - self.rect.width):
			self.rect.x = self.screen.get_width() - self.rect.width
		if self.rect.y <= 0:
			self.rect.y = 0
		if self.rect.y >= (self.screen.get_height() - self.rect.height):
			self.rect.y = self.screen.get_height() - self.rect.height

	def move(self):
		"""
		Moves the sprite on its generated path & direction.
		"""
		# tu dong di chuyen
		self.rect.y += self.y
		self.rect.x += self.x

		if self.rect.x <= 0:
			self.rect.x = 0
			self.x = -self.x
		elif self.rect.x >= (self.screen.get_width() - self.rect.width):
			self.rect.x = self.screen.get_width() - self.rect.width
			self.x = -self.x
		elif self.rect.y <= 0:
			self.rect.y = 0
			self.y = -self.y
		elif self.rect.y >= (self.screen.get_height() - self.rect.height):
			self.rect.y = self.screen.get_height() - self.rect.height
			self.y = -self.y

	def shoot(self, direction):
		"""
		Shoots a bullet in a random direction.
		"""
		die = direction
		bullet = game_items.Bullet(self.screen, die, self.rect.centerx, self.rect.centery, "ufo", False)
		self.bullets_sprite_list.add(bullet)
		self.game.all_sprite_list.add(bullet)
