import pygame

# dimentions
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

# colors
WHITE = (255, 255, 255)

# background
BACKGROUND_MENU = "./image/background.png"
BACKGROUND_PLAY = "./image/grass.jpg"

# cac' tham so cua game
PLAYER_HP = 1000
ENEMY_HP = 100
ENEMY_MIN = 50 # thoi gian xuat hien quai
ENEMY_MAX = 300
HEALTH_MIN = 800 # thoi gian xuat hien tui' mau'
HEALTH_MAX = 1200
HEALTH_BOOST_MIN = 50
HEALTH_BOOST_MAX = 300

# cac' tham so' cua tank
SPEED_TANK = 5
BULLET_COUNTER = 3 # thoi gian dan cach giua 2 lan ban sung 
AMMO = 500

# cac hinh cua xe tang
TANK_IMAGE_0 = "./image/tankp1/TN3.png"
TANK_IMAGE_1 = "./image/tankp1/TE3.png"
TANK_IMAGE_2 = "./image/tankp1/TS3.png"
TANK_IMAGE_3 = "./image/tankp1/TW3.png"
TANK_IMAGE_4 = "./image/tankp1/TNW3.png"
TANK_IMAGE_5 = "./image/tankp1/TSW3.png"
TANK_IMAGE_6 = "./image/tankp1/TSE3.png"
TANK_IMAGE_7 = "./image/tankp1/TNE3.png"

# item giup nhan vat trong game
HEALTH_IMAGE = "./image/item/health.png"
AMMO_IMAGE = "./image/item/ammo.png"
AMMO_BOOST_MIN = 100 # tang dan. se~ ngau nhien trong khoang nay 
AMMO_BOOST_MAX = 200

# enemy
ENEMY_IMAGE = "./image/enemy/ufo.png"
ENEMY_SPEED_MIN = 1
ENEMY_SPEED_MAX = 5
ENEMY_MIN_BULLET_SPEED = 50 # toc do vien dan 
ENEMY_MAX_BULLET_SPEED = 100

# explosions
EXPLOSION_IMAGE = "./image/item/explosion.png"
BIG_EXPLOSION_IMAGE = "./image/item/bigexp.png"

# bullet
BULLET_ENEMY = "./image/bullet/bullet_enemy.png"
BULLET_PLAYER_NORMAL = "./image/bullet/bullet_player_normal.png"
BULLET_PLAYER_RAPID = "./image/bullet/bullet_player_rapid.png"
BULLET_SPEED = 10

