import pygame
import random
import constant

# la vat dung de tang mau
class HealthBox(pygame.sprite.Sprite):
	def __init__(self, screen):
		pygame.sprite.Sprite.__init__(self)
		self.screen = screen
		# hinh`, toa. do xuat hien., tang mau', thoi` gian x
		self.image = pygame.image.load(constant.HEALTH_IMAGE)
		self.rect = self.image.get_rect()
		self.rect.x = random.randint(0, screen.get_width() - self.rect.width)
		self.rect.y = random.randint(0, screen.get_height() - self.rect.height)
		self.healthboost = random.randint(constant.HEALTH_BOOST_MIN, constant.HEALTH_BOOST_MAX)
		self.tolive = 400

	def update(self):
		"""
		Allows the game to update this sprite.
		"""
		self.tolive -= 1
		# het thoi gian thi no' mat 
		if self.tolive == 0:
			self.collided()

	def collided(self):
		"""
		Ensures that if this sprite hits something, it will be destroyed.
		"""
		self.kill()

class AmmoBox(pygame.sprite.Sprite):
    """
    Class representing an ammo box, another upgrade generated at random, which gives a boost to player ammo.
    """

    def __init__(self, screen):
        """
        Constructor for ammo box, loads image and generates random position, ammo boost and lifetime for this sprite.
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(constant.AMMO_IMAGE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen.get_width())
        self.rect.y = random.randint(0, screen.get_height())
        self.ammoboost = random.randint(constant.AMMO_BOOST_MIN, constant.AMMO_BOOST_MAX)
        self.tolive = 400

    def update(self):
        """
        Allows the game to update this sprite.
        """
        self.tolive -= 1
        if self.tolive == 0:
            self.collided()

    def collided(self):
        """
        Ensures that if this sprite has collided, it will be destroyed.
        """
        self.kill()

    def get_name(self):
        """
        Returns the name of this upgrade.
        """
        return "ammo"

class Explosion(pygame.sprite.Sprite):
	def __init__(self, screen, xpos, ypos, size):
		pygame.sprite.Sprite.__init__(self)
		self.screen = screen
		if size == "small":
			self.image = pygame.image.load(constant.EXPLOSION_IMAGE)
		else:
			self.image = pygame.image.load(constant.BIG_EXPLOSION_IMAGE)

		# vi tri
		self.rect = self.image.get_rect()
		self.rect.centerx = xpos
		self.rect.centery = ypos

		# thoi gian tao. hieu ung no
		self.lifemax = 10
		self.lifecounter = 0

	def update(self):
		"""
		Allows the game to update this sprite.
		"""
		self.lifecounter += 1
		if self.lifecounter == self.lifemax:
			self.kill()

class Bullet(pygame.sprite.Sprite):
	def __init__(self, screen, direction, xpos, ypos, side, rapidFire):
		pygame.sprite.Sprite.__init__(self)

		self.screen = screen
		# neu dan cua? dich, neu dan cua ta () truong hop ban' thuong` or ban' nhanh
		if side == "ufo":
			self.image = pygame.image.load(constant.BULLET_ENEMY)
		if side == "tank":
			if rapidFire:
				self.image = pygame.image.load(constant.BULLET_PLAYER_RAPID)
			else:
				self.image = pygame.image.load(constant.BULLET_PLAYER_NORMAL)

		# vi tri cua vien dan
		self.rect = self.image.get_rect()
		self.rect.centerx = xpos
		self.rect.centery = ypos

		self.x = 0 # bien' chi? toc do cung nhu huong di chuyen cua vien dan 
		self.y = 0
		self.die = direction
		self.flight_path()
		self.set_position()

	def flight_path(self):
		if self.die == "n":
			self.x = 0
			self.y = -constant.BULLET_SPEED
		if self.die == "s":
			self.x = 0
			self.y = constant.BULLET_SPEED
		if self.die == "w":
			self.x = -constant.BULLET_SPEED
			self.y = 0
		if self.die == "e":
			self.x = constant.BULLET_SPEED
			self.y = 0
		if self.die == "nw":
			self.x = -constant.BULLET_SPEED
			self.y = -constant.BULLET_SPEED
		if self.die == "ne":
			self.x = constant.BULLET_SPEED
			self.y = -constant.BULLET_SPEED
		if self.die == "sw":
			self.x = -constant.BULLET_SPEED
			self.y = constant.BULLET_SPEED
		if self.die == "se":
			self.x = constant.BULLET_SPEED
			self.y = constant.BULLET_SPEED

	def set_position(self):
		"""
		Sets the position of the bullet relative to the tank sprite which fired it.
		"""
		if self.die == "n":
			self.rect.centerx += -1
			self.rect.centery += -25
		elif self.die == "e":
			self.rect.centerx += 35
			self.rect.centery += -14
		elif self.die == "s":
			self.rect.centerx += -2
			self.rect.centery += 25
		elif self.die == "w":
			self.rect.centerx += -9
			self.rect.centery += -15
		elif self.die == "nw":
			self.rect.centerx += -6
			self.rect.centery += -20
		elif self.die == "ne":
			self.rect.centerx += 26
			self.rect.centery += -22
		elif self.die == "sw":
			self.rect.centerx += -8
			self.rect.centery += 14
		elif self.die == "se":
			self.rect.centerx += 29
			self.rect.centery += 14

	def boundaries(self):
		"""
		Ensures that when this bullet hits a screen boundary, it is immediately destroyed.
		"""
		if(self.rect.x <= 0 or self.rect.x >= (self.screen.get_width()-self.rect.width) or self.rect.y <= 0 or self.rect.y >= (self.screen.get_height()-self.rect.height)):
			self.kill()

	def update(self):
		"""
		Allows a game to update this sprite.
		"""
		self.boundaries()
		self.rect.centery += self.y
		self.rect.centerx += self.x