import one_player
import pygame
import constant


class Game():
	def __init__(self):
		pygame.init()

		# set the height and width of the screen
		self.screen_width = constant.SCREEN_WIDTH
		self.screen_height = constant.SCREEN_HEIGHT
		self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])

		# load font
		self.font = pygame.font.Font("./font/Purisa.ttf", 35)

		# clock
		self.clock = pygame.time.Clock()


	def runGame(self):
		# set default settings for games
		running = True
		game_mode = "1player"
		difficulty = "easy"
		background = pygame.image.load(constant.BACKGROUND_MENU)

		while running:
			# listen for events
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = false
				elif event.type == pygame.KEYDOWN:
					keys = pygame.key.get_pressed()
					if keys[pygame.K_1]:
						self.playGame(one_player.OnePlayer(self.screen))
					#elif keys[pygame.K_2]:
						#self.playGame(two_player.TwoPlayer(screen, difficulty))
					#elif keys[pygame.K_3]:
						#self.playGame(coop.Cooperative(screen, difficulty))

			# output to the screen
			self.screen.blit(background, (0, 0))
			pygame.display.flip()
			self.clock.tick(30)

	def playGame(self, game):
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False 
				elif event.type == pygame.KEYDOWN:
					key = pygame.key.get_pressed()
					# if a player pressed P --> so pause, esc --> out 
					#if key[pygame.K_p]
			# if the player die , so running = False
			
			# let's play that game, all of things in game would appear
			game.update()

			self.clock.tick(30)

if __name__ == "__main__":
	game = Game()
	game.runGame()
	pygame.quit()