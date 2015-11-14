import pygame
import constant
import random
import tank
import game_items
import enemy

import game_modes

# class representing one player game mode
class OnePlayer(game_modes.GameMode):
	def __init__(self, screen):
		game_modes.GameMode.__init__(self, screen)
		self.screen = screen

		# game cua? ta gom` cac' loai.  tham so' sau
		self.p1_core = 0 # diem? nguoi choi
		self.p1_hp = constant.PLAYER_HP # mau' cua nguoi choi
		self.enemy_hp = constant.ENEMY_HP # mau' cua ke thu`

		self.enemy_interval = random.randint(constant.ENEMY_MIN, constant.ENEMY_MAX) # thoi gian xuat hien enemy 
		self.health_interval = random.randint(constant.HEALTH_MIN, constant.HEALTH_MAX) # thoi gian xuat hien tui' mau'
		self.ammo_interval = random.randint(constant.HEALTH_MIN, constant.HEALTH_MAX) # thoi gian xuat hien tui' mau'

		# cac loai sprite trong game
		self.enemy_sprite_list = pygame.sprite.Group()
		self.upgrades_sprite_list = pygame.sprite.Group()
		self.explosions_sprite_list = pygame.sprite.Group()
		self.all_sprite_list = pygame.sprite.Group()
		self.player = tank.Player1Tank(self)
		self.all_sprite_list.add(self.player)

	# override buoc 1
	def generate_game_items(self):
		print 'Buoc 1'
		# cu' giam dan` thoi` gian tao. do` vat. va enemy , khi bang 0 thi tao cai moi'
		self.health_interval -= 1
		self.ammo_interval -= 1
		self.enemy_interval -= 1
		if self.health_interval == 0:
			item_obj = game_items.HealthBox(self.screen)
			self.upgrades_sprite_list.add(item_obj)
			self.all_sprite_list.add(item_obj)
			self.health_interval = random.randint(constant.HEALTH_MIN, constant.HEALTH_MAX)
		
		if self.ammo_interval == 0:
			item_obj = game_items.AmmoBox(self.screen)
			self.upgrades_sprite_list.add(item_obj)
			self.all_sprite_list.add(item_obj)
			self.ammo_interval = random.randint(constant.HEALTH_MIN, constant.HEALTH_MAX)

		if self.enemy_interval == 0:
			enemy_obj = enemy.Enemy(self)
			self.enemy_sprite_list.add(enemy_obj)
			self.all_sprite_list.add(enemy_obj)
			self.enemy_interval = random.randint(constant.ENEMY_MIN, constant.ENEMY_MAX)


	# override buoc 2
	def handle_collisions(self):
		print 'Buoc 2'
		# neu xe tang dung trung vat bom mau hay ammo thi tang mau cho xe tang, xoa' vat bom mau, tang dan. , xoa' dan.
		upgrade_hit_list = pygame.sprite.spritecollide(self.player, self.upgrades_sprite_list, False)
		for upgrade in upgrade_hit_list:
			if upgrade.get_name() == "health":
				self.p1_hp += upgrade.healthboost
				upgrade.kill()
			elif upgrade.get_name() == "ammo":
				self.player.ammo += upgrade.ammoboost
				upgrade.kill()

		# neu xe tang dung trung ke dich, xoa' ke dich, tang score, lam` hieu. ung' no?, giam mau' ke thu
		enemy_hit_list = pygame.sprite.spritecollide(self.player, self.enemy_sprite_list, False)
		for enemy in enemy_hit_list:
			self.p1_core += self.enemy_hp
			self.p1_hp -= 100
			ex_obj = game_items.Explosion(self.screen, enemy.rect.centerx, enemy.rect.centery, "big")
			self.explosions_sprite_list.add(ex_obj)
			self.all_sprite_list.add(ex_obj)
			enemy.kill()

		# neu' enemy bi het' mau' thi no?
		# lap. tung` enemy va` lap. tung` cuc. dan. cua? enemy
		for enemy in self.enemy_sprite_list:
			if enemy.hp <= 0:
				ex_obj = game_items.Explosion(self.screen, enemy.rect.centerx, enemy.rect.centery, "big")
				self.explosions_sprite_list.add(ex_obj)
				self.all_sprite_list.add(ex_obj)
				enemy.kill()
			# neu dan. cua dich. trung ta.
			bullets_hit_list = pygame.sprite.spritecollide(self.player, enemy.bullets_sprite_list, False)
			for bullet in bullets_hit_list:
				ex_obj = game_items.Explosion(self.screen, bullet.rect.centerx, bullet.rect.centery, "small")
				self.explosions_sprite_list.add(ex_obj)
				self.all_sprite_list.add(ex_obj)
				bullet.kill()
				self.p1_hp -= 25
			# check neu' cua? ta trung dich
			bullet_hit_list = pygame.sprite.spritecollide(enemy, self.player.bullets_sprite_list, False)
			for bullet in bullet_hit_list:
				ex_obj = game_items.Explosion(self.screen, bullet.rect.centerx, bullet.rect.centery, "small")
				self.explosions_sprite_list.add(ex_obj)
				self.all_sprite_list.add(ex_obj)
				enemy.hp -= 10
				self.p1_core += 100
				bullet.kill()

	# override buoc 3
	def update_sprites(self):
		print 'Buoc 3'
		self.all_sprite_list.update()

	# override buoc 4
	def draw_changes(self):
		print 'Buoc 4'
		self.all_sprite_list.draw(self.screen)

	# override buoc 5
	def display_game_message(self):
		print 'Buoc 5'

	# override buoc 6
	def check_for_game_over(self):
		print 'Buoc 6'
