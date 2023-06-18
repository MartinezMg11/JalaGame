import random
import pygame
from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet
from game.utils.constants import DEFAULT_TYPE, FONT_GAME, GAME_OVER, HEART, LASER_SONIDO, SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP

class Spaceship(Sprite):
    SHIP_WIDTH = 40
    SHIP_HEIGHT = 60
    X_POS = (SCREEN_WIDTH // 2) - SHIP_WIDTH
    Y_POS = 500
    SHIP_SPEED = 10

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.SHIP_WIDTH, self.SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = 'player'
        self.power_up_type = DEFAULT_TYPE
        self.has_power_up = False
        self.power_time_up = 0
        self.lives = 3
        



    def update(self, user_input,game):
        self.shoot(game.bullet_manager,user_input)
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()
        

    def move_left(self):
        self.rect.x -= self.SHIP_SPEED
        if self.rect.left < 0:
            self.rect.x = SCREEN_WIDTH - self.SHIP_WIDTH

    def move_right(self):
        self.rect.x += self.SHIP_SPEED
        if self.rect.right >= SCREEN_WIDTH - self.SHIP_WIDTH:
            self.rect.x = 0

    def move_up(self):
        if self.rect.y > 0:
            self.rect.y -= self.SHIP_SPEED

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 70:
            self.rect.y += self.SHIP_SPEED

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def shoot(self, bullet_Manager,user_input):
        if user_input[pygame.K_SPACE]:
                LASER_SONIDO.play()
                bullet = Bullet(self)
                bullet_Manager.add_bullet(bullet)

    def set_image(self, size = (SHIP_WIDTH, SHIP_HEIGHT), image = SPACESHIP):
        self.image = image
        self.image = pygame.transform.scale(self.image,size)

    def subtract_lives(self,screen):
        if self.lives > 0:
            self.lives -= 1
        font = pygame.font.Font(FONT_GAME, 20)
        text = font.render(f"Vidas Restantes: {self.lives}", True, (255, 255, 255))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        
        if self.lives >= 1:
            screen.blit(text, text_rect)
        else:
            screen.blit(GAME_OVER, text_rect)

        pygame.display.update()
        pygame.time.delay(1000)
    
    def lives_restart(self):
        self.lives = 3

    def draw_lives(self,screen):
        heart_list =[1080,1050,1020,990,960,930,900,870,840,810,780,750]

        heart_rect = HEART.get_rect()
        heart_rect.center = (heart_list[0], 580)
        screen.blit(HEART, heart_rect.center)

        if self.lives >= 2:
            heart_rect.center = (heart_list[1], 580)
            screen.blit(HEART, heart_rect.center)
        if self.lives >= 3:
            heart_rect.center = (heart_list[2], 580)
            screen.blit(HEART, heart_rect.center)
        if self.lives >= 4:
            heart_rect.center = (heart_list[3], 580)
            screen.blit(HEART, heart_rect.center)
        if self.lives >= 5:
            heart_rect.center = (heart_list[4], 580)
            screen.blit(HEART, heart_rect.center)
        if self.lives >= 6:
            heart_rect.center = (heart_list[5], 580)
            screen.blit(HEART, heart_rect.center)
        if self.lives >= 7:
           heart_rect.center = (heart_list[6], 580)
           screen.blit(HEART, heart_rect.center)
        if self.lives >= 8:
           heart_rect.center = (heart_list[7], 580)
           screen.blit(HEART, heart_rect.center)
        if self.lives >= 9:
           heart_rect.center = (heart_list[8], 580)
           screen.blit(HEART, heart_rect.center)

        pygame.display.update()