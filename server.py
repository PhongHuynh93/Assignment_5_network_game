# the Server can:
# any clients connect to it, print hello new player 
# all of players can see each other hay their bullet  .....
import PodSixNet.Channel
import PodSixNet.Server
from time import sleep

class ClientChannel(PodSixNet.Channel.Channel):
	

	#receive position of a "bullet" of a client, and send back data 
	def Network_Bullet(self, data):
		bullet_x = data["bullet_x"]
		bullet_y = data["bullet_y"]
		index = data["index"]
		self._server.sendPositionBullet(bullet_x, bullet_y, index)

	# receive postion of a player 
	def Network_PlayerPosition(self, data):
		index_player = data["index_player"]
		player_x = data["player_x"]
		player_y = data["player_y"]
		self._server.sendPositionPlayer(player_x, player_y, index_player)

class BoxesServer(PodSixNet.Server.Server):

	channelClass = ClientChannel

	def __init__(self, *args, **kwargs):
		PodSixNet.Server.Server.__init__(self, *args, **kwargs)
		# the number of player
		self.index_player = 0
		self.game = None # array of channel (client)

	# Called when a new player connected to server
	def Connected(self, channel, addr):
		print 'new connection:', channel, addr
		
		# if only one player, make a Game
		if self.index_player == 0:
			self.game = Game(channel, self.index_player)
		else:
			# if >= 1 player, add that player to Game, send that player to the other clients so they can see him.
			print 'hello new Player', str(self.index_player)
			self.game.player.append(channel)

		# send back id to the client 
		self.game.player[self.index_player].Send({"action" : "IndexPlayer", "index_player": self.index_player})

		# other players must see each other
		self.index_player += 1
		for main_player in range(self.index_player):
			for other_player in range(self.index_player):
				if main_player != other_player:
					self.game.player[main_player].Send({"action" : "OtherPlayer", "index_player_other" : other_player})
		self.game.index_player = self.index_player
		
	def sendPositionBullet(self, bullet_x, bullet_y, index):
		self.game.sendPositionBullet(bullet_x, bullet_y, index)

	def sendPositionPlayer(self, player_x, player_y, index_player):
		self.game.sendPositionPlayer(player_x, player_y, index_player)


class Game:
	def __init__(self, channel, index_player):
		print 'hello new Player', index_player
		self.index_player = index_player
		self.player = [] # list that include players
		self.player.append(channel)

	# send back to all of player 
	def sendPositionBullet(self, bullet_x, bullet_y, index):
		for i in range(self.index_player):
			if i != index: 
				self.player[i].Send({"action" : "BulletPosition", "bullet_x": bullet_x, "bullet_y": bullet_y, "index" : i})

	# send back position of all of players in game to clients
	def sendPositionPlayer(self, player_x, player_y, index_player):
		for i in range(self.index_player):
			if i != index_player:
				self.player[i].Send({"action" : "PlayerPosition", "player_x" : player_x, "player_y" : player_y, "index" : index_player})

print "STARTING SERVER ON LOCALHOST"
boxesServe=BoxesServer()
while True:
	boxesServe.Pump()
	sleep(0.01)