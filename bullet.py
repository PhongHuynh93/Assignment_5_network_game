import pygame
import random
from PodSixNet.Connection import ConnectionListener, connection
from time import sleep

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
# --- Classes
class Block(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self, color):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
 
        self.image = pygame.Surface([20, 15])
        self.image.fill(color)
 
        self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """
 
    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
 
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
 
        self.rect = self.image.get_rect()
        self.rect.y = 370
        self.rect.x = 100 
 
    def update(self):
        """ Update the player's position. """, self
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()
 
        # Set the player x position to the mouse x position
        self.rect.x = pos[0]
 
class Player_Other(pygame.sprite.Sprite):
    def __init__(self, index):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
 
        self.rect = self.image.get_rect()
        self.rect.y = 370
        self.rect.x = 100 
        self.index = index

    #def update(self):


class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
 
        self.image = pygame.Surface([4, 10])
        self.image.fill(BLACK)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Move the bullet. """
        self.rect.y -= 3
 

class Game(ConnectionListener):
    def __init__(self):
        # --- Create the window
         
        # Initialize Pygame
        pygame.init()

        # Set the height and width of the screen
        self.screen_width = 700
        self.screen_height = 400
        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])
         
        # --- Sprite lists
         
        # This is a list of every sprite. All blocks and the player block as well.
        self.all_sprites_list = pygame.sprite.Group()
         
        # List of each block in the game
        self.block_list = pygame.sprite.Group()
         
        # List of each bullet
        self.bullet_list = pygame.sprite.Group()
         
        # --- Create the sprites
         
        for i in range(50):
            # This represents a block
            block = Block(BLUE)
         
            # Set a random location for the block
            block.rect.x = random.randrange(self.screen_width)
            block.rect.y = random.randrange(350)
         
            # Add the block to the list of objects
            self.block_list.add(block)
            self.all_sprites_list.add(block)
         
        # Create a red player block
        self.player = Player()
        self.all_sprites_list.add(self.player)

        self.other_player_list = [] # list of index of other players
         
        self.score = 0
        

        self.index_player = 0 # id of main player on a network

        self.Connect() # connect to server 


    def runGame(self):
        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()
        # Loop until the user clicks the close button.
        done = False
        pos = 0
        # -------- Main Program Loop -----------
        while not done:
            # --- Network
            connection.Pump()
            self.Pump()
            # --- Event Processing
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
         
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Fire a bullet if the user clicks the mouse button
                    bullet = Bullet()
                    # Set the bullet so it is where the player is
                    bullet.rect.x = self.player.rect.x
                    bullet.rect.y = self.player.rect.y
                    # Add the bullet to the lists
                    self.all_sprites_list.add(bullet)
                    self.bullet_list.add(bullet)
                    # send x, y of bullet to server 
                    self.Send({"action" : "Bullet", "bullet_x" : bullet.rect.x, "bullet_y" : bullet.rect.y, "index" : self.index_player})

            # send postion of main player to server
            pos = pygame.mouse.get_pos()
            self.Send({"action" : "PlayerPosition", "index_player" : self.index_player, "player_x" : pos[0], "player_y" : pos[1]})
         
            # --- Game logic
         
            # Call the update() method on all the sprites
            self.all_sprites_list.update()
         
            # Calculate mechanics for each bullet
            for bullet in self.bullet_list:
         
                # See if it hit a block
                block_hit_list = pygame.sprite.spritecollide(bullet, self.block_list, True)
         
                # For each block hit, remove the bullet and add to the score
                for block in block_hit_list:
                    self.bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)
                    self.score += 1
         
                # Remove the bullet if it flies up off the screen
                if bullet.rect.y < -10:
                    self.bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)
         

            # --- Draw a frame
         
            # Clear the screen
            self.screen.fill(WHITE)
         
            # Draw all the spites
            self.all_sprites_list.draw(self.screen)
         
            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
         
            # --- Limit to 20 frames per second
            clock.tick(60)

    # take id of a player
    def Network_IndexPlayer(self, data):
        self.index_player = data["index_player"]
        print "Im a Player", str(self.index_player) # output index_player in client cmmd

    # take bullet from other player
    def Network_BulletPosition(self, data):
        bullet = Bullet()
        # Set the bullet so it is where the player is
        bullet.rect.x = data["bullet_x"]
        bullet.rect.y = data["bullet_y"]
        # Add the bullet to the lists
        self.all_sprites_list.add(bullet)
        self.bullet_list.add(bullet)

    # take new player
    def Network_OtherPlayer(self, data):
        player = Player_Other(data["index_player_other"])
        self.other_player_list.append(player)
        self.all_sprites_list.add(player)

    # take position
    def Network_PlayerPosition(self, data):
        for player in self.other_player_list:
            if player.index == data["index"]:
                player.rect.x = data["player_x"]

if __name__ == "__main__":
    game = Game()
    game.runGame()
    pygame.quit()

