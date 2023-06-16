import pygame
from game.components.bullets.bullet_manager import BulletManager
from game.components.enemies.enemy_manager import EnemyManager
from game.components.menu import Menu

from game.utils.constants import BG, FONT_GAME,GAME_OVER, HEART, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from game.components.spaceship import Spaceship

class Game:


    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running= False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.death_count = 0
        self.score = 0
        self.score_total = 0
        self.lives = 3
        self.lives_count = 0
        self.menu = Menu('Press Any key to start...',self.screen)

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
                #implementar
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.score = 0
        self.bullet_manager.reset() #implementar
        self.enemy_manager.reset() #implementar
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False


    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input,self)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)



    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.draw_score()
        self.draw_lives()
        pygame.display.update()
        #pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
            
        self.y_pos_bg += self.game_speed

    def show_menu(self):
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2

        self.menu.reset_screen_color(self.screen)

        if self.death_count > 0:
            self.menu.update_message(f'Vidas Perdidas:{self.lives_count}  Score Total:{self.score_total}')
            self.lives_restart()

        icon = pygame.transform.scale(ICON,(80,120))
        self.screen.blit(icon,(half_screen_width - 50,half_screen_height - 150))
        self.menu.draw(self.screen)
        self.menu.update(self)



    def draw_score(self):
        font = pygame.font.Font(FONT_GAME,15)
        text = font.render(f'Score: {self.score}',True,(255,255,255))
        text_rect = text.get_rect()
        text_rect.center = (1000,20)
        self.screen.blit(text,text_rect)

    def subtract_lives(self):
        if self.lives > 0:
            self.lives -= 1
        font = pygame.font.Font(FONT_GAME, 20)
        text = font.render(f"Vidas Restantes: {self.lives}", True, (255, 255, 255))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        
        if self.lives >= 1:
            self.screen.blit(text, text_rect)
        else:
            self.screen.blit(GAME_OVER, text_rect)

        pygame.display.update()
        pygame.time.delay(1000)


    def draw_lives(self):
        heart_rect1 = HEART.get_rect()
        heart_rect1.center = (1080, 580)
        heart_rect2 = HEART.get_rect()
        heart_rect2.center = (1050, 580)
        heart_rect3 = HEART.get_rect()
        heart_rect3.center = (1020, 580)
        self.screen.blit(HEART, heart_rect1)

        if self.lives >= 2:
            self.screen.blit(HEART, heart_rect2)

        if self.lives == 3:
            self.screen.blit(HEART, heart_rect3)

        pygame.display.update()

    def lives_restart(self):
        self.lives = 3