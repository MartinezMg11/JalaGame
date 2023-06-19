import pygame
import os
pygame.mixer.init()
# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
HEART_TYPE = 'heart'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))


EXPLOSION_1 = pygame.image.load(os.path.join(IMG_DIR, "Explosion/1.png"))
EXPLOSION_2 = pygame.image.load(os.path.join(IMG_DIR, "Explosion/2.png"))
EXPLOSION_3 = pygame.image.load(os.path.join(IMG_DIR, "Explosion/3.png"))
EXPLOSION_4 = pygame.image.load(os.path.join(IMG_DIR, "Explosion/4.png"))
EXPLOSION_5 = pygame.image.load(os.path.join(IMG_DIR, "Explosion/5.png"))
EXPLOSION_6 = pygame.image.load(os.path.join(IMG_DIR, "Explosion/6.png"))
EXPLOSION_7 = pygame.image.load(os.path.join(IMG_DIR, "Explosion/7.png"))
EXPLOSION_8 = pygame.image.load(os.path.join(IMG_DIR, "Explosion/8.png"))
EXPLOSION_9 = pygame.image.load(os.path.join(IMG_DIR, "Explosion/9.png"))
EXPLOSION_10 = pygame.image.load(os.path.join(IMG_DIR, "Explosion/10.png"))
EXPLOSION_11 = pygame.image.load(os.path.join(IMG_DIR, "Explosion/10.png"))
EXPLOSION_12 = pygame.image.load(os.path.join(IMG_DIR, "Explosion/10.png"))

FONT_GAME = os.path.join(IMG_DIR,'Other/AtariClassicChunky-PxXP.ttf')
FONT_TITLE = os.path.join(IMG_DIR,'Other/MinecraftEvenings-RBao.ttf')
FONT_STYLE = 'freesansbold.ttf'

SOUND_PRINCIPAL =pygame.mixer.Sound(os.path.join(IMG_DIR,'Sounds/Intergalactic Odyssey.ogg'))
LASER_SONIDO = pygame.mixer.Sound(os.path.join(IMG_DIR,'Sounds/laser.wav'))
EXPLOSION_SONIDO = pygame.mixer.Sound(os.path.join(IMG_DIR,'Sounds/explosion.wav'))

SOUND_PRINCIPAL.set_volume(0.2)