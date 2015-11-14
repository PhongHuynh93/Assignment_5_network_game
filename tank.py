import pygame
import constant
import game_items

class PlayerTank(object):
	def __init__(self, game):
		self.speed = constant.SPEED_TANK
		self.game = game
		self.screen = self.game.screen


		# hinh`, vi tri cua xe tang 
		self.rect = self.image.get_rect() # image tu` class con 
		self.rect.centerx = 23 
		self.rect.centery = 45

		# tao. list dan. cua chiec xe tang
		self.bullets_sprite_list = pygame.sprite.Group()
		self.ammo = constant.AMMO

		# thong^ so' lien quan den' dan. cua xe tang
		self.bullet_counter = 0 # thoi` gian cho phep dc ban' dan.
		self.can_shoot = False  # bien' cho phep ban' dan.

		self.rapidFire = False # co' the ban' dan toc do. cao ko ?

	# thoi gian giua~ 2 lan ban' dan se quyet dinh. co duoc ban' ko, con ban' nhanh ko can rang buoc. thoi gian
	# check vi. tri' cua xe tang co' vuot. ngoai` man` hinh` chua
	def update(self):
		if not self.can_shoot and not self.rapidFire:
			self.bullet_counter += 1
		if self.bullet_counter == constant.BULLET_COUNTER and not self.rapidFire:
			self.can_shoot = True
			self.bullet_counter = 0


		self.boundaries()

	def boundaries(self):
		if self.rect.x <= 0:
			self.rect.x = 0
		if self.rect.x >= (self.screen.get_width() - self.rect.width):
			self.rect.x = self.screen.get_width() - self.rect.width
		if self.rect.y <= 0:
			self.rect.y = 0
		if self.rect.y >= (self.screen.get_height() - self.rect.height):
			self.rect.y = self.screen.get_height() - self.rect.height

	def control_tank(self):
		raise Exception('Abstract method, please override in the subclass')

	# ban sung theo huong, tao sprite bullet va` add vao` sprite 
	def shoot(self, direction):
		bullet = game_items.Bullet(self.screen, direction, self.rect.centerx, self.rect.centery, "tank", self.rapidFire)
		self.bullets_sprite_list.add(bullet)
		self.game.all_sprite_list.add(bullet)
		self.ammo -= 1



class Player1Tank(PlayerTank, pygame.sprite.Sprite):
	def __init__(self, game):
		pygame.sprite.Sprite.__init__(self)

		self.imgs = []
		# bien' chua' hinh cua game
		self.imgs.append(pygame.image.load(constant.TANK_IMAGE_0))
		self.imgs.append(pygame.image.load(constant.TANK_IMAGE_1))
		self.imgs.append(pygame.image.load(constant.TANK_IMAGE_2))
		self.imgs.append(pygame.image.load(constant.TANK_IMAGE_3))
		self.imgs.append(pygame.image.load(constant.TANK_IMAGE_4))
		self.imgs.append(pygame.image.load(constant.TANK_IMAGE_5))
		self.imgs.append(pygame.image.load(constant.TANK_IMAGE_6))
		self.imgs.append(pygame.image.load(constant.TANK_IMAGE_7))

		# bien' chua' hinh` default khi load xe tank
		self.image = pygame.image.load(constant.TANK_IMAGE_0)

		PlayerTank.__init__(self, game)

	
	def update(self):
		PlayerTank.update(self) # using "update()" in its superclass do class con va cha deu co method update()
		self.control_tank()

	# move tank
	def control_tank(self):
		keys = pygame.key.get_pressed()
		# go straight
		if keys[pygame.K_w]: # di len
			self.image = self.imgs[0]
			self.rect.centery -= self.speed
			self.facing = "n"
		if keys[pygame.K_s]: # di xuong
			self.image = self.imgs[2]
			self.rect.centery += self.speed
			self.facing = "s"
		if keys[pygame.K_a]: # di qua trai
			self.image = self.imgs[3]
			self.rect.centerx -= self.speed
			self.facing = "w"
		if keys[pygame.K_d]: # di qua phai
			self.image = self.imgs[1]
			self.rect.centerx += self.speed
			self.facing = "e"

		# di cheo, khi di tu` da~ update vi. tri o? tren roi` nen 4 dong` sau chi? load hinh`
		if keys[pygame.K_w] and keys[pygame.K_a]: # di cheo len ben trai
			self.image = self.imgs[4]
			self.facing = "nw"
		if keys[pygame.K_s] and keys[pygame.K_a]: # di cheo xuong ben trai
			self.image = self.imgs[5]
			self.facing = "sw"
		if keys[pygame.K_w] and keys[pygame.K_d]: # di cheo len ben phai
			self.image = self.imgs[7]
			self.facing = "ne"
		if keys[pygame.K_s] and keys[pygame.K_d]: # di cheo len xuong phai 
			self.image = self.imgs[6]
			self.facing = "se"

		# ban' sung
		if keys[pygame.K_SPACE] and (self.can_shoot or self.rapidFire) and self.ammo > 0:
			self.shoot(self.facing)
			self.can_shoot = False

		# neu' nhan' f la bat tat ban' nhanh
		if keys[pygame.K_f]:
			if self.rapidFire: # doi sang ban' thuong
				self.rapidFire = False
			elif not self.rapidFire: # ban nhanh
				self.rapidFire = True



