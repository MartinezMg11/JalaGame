import pygame
from game.utils.constants import BG, ENEMY_1, ENEMY_2, FONT_GAME, FONT_TITLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH


class Menu:
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2

    def __init__(self,message,screen,message1='',message2='',message3='',TITLE = "SPACESHIP"):
        screen.fill((255,255,255))
        self.font = pygame.font.Font(FONT_GAME,30)
        self.font_title = pygame.font.Font(FONT_TITLE,100)
        self.font_results = pygame.font.Font(FONT_TITLE,40)
        self.title = self.font_title.render(TITLE,True,(255,255,255))
        self.title_rect = self.title.get_rect()
        self.title_rect.center = (self.HALF_SCREEN_WIDTH,50)
        self.text = self.font.render(message,True,(255,255,255))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH,self.HALF_SCREEN_HEIGHT * 2 - 50)
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.text1 = self.font.render(message1,True,(255,255,255))
        self.text2 = self.font.render(message2,True,(255,255,255))
        self.text3 = self.font.render(message3,True,(255,255,255))
        self.text_rect1 = self.text.get_rect()
        self.text_rect1.center = (self.HALF_SCREEN_WIDTH,self.HALF_SCREEN_HEIGHT-200)
        self.text_rect2 = self.text.get_rect()
        self.text_rect2.center = (self.HALF_SCREEN_WIDTH,self.HALF_SCREEN_HEIGHT-400)
        self.text_rect3 = self.text.get_rect()
        self.text_rect3.center = (self.HALF_SCREEN_WIDTH,self.HALF_SCREEN_HEIGHT-600)

    def update(self,game):
        pygame.display.update()
        self.handle_events_on_menu(game)
       

    def draw(self,screen):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        screen.blit(self.text, self.text_rect)
        screen.blit(self.title, self.title_rect)
        screen.blit(self.text1, self.text_rect1.center)
        screen.blit(self.text2, self.text_rect2.center)
        screen.blit(self.text3, self.text_rect3.center)

    def draw_icons(self,screen):
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2
        icon = pygame.transform.scale(ICON, (250, 350))
        icon2 = pygame.transform.scale(ENEMY_1, (250, 300))
        icon3 = pygame.transform.scale(ENEMY_2, (250, 300))
        screen.blit(icon2, (half_screen_width - 400, half_screen_height - 100))
        screen.blit(icon, (half_screen_width - 100, half_screen_height - 200))
        screen.blit(icon3, (half_screen_width + 200, half_screen_height - 100))

    def handle_events_on_menu(self,game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running= False
            elif event.type == pygame.KEYDOWN:
                game.run()

    def reset_screen_color(self,screen):
        screen.fill((255,255,255))


    def update_message(self, message1,message2,message3):
        self.text = self.font.render('Press any key to start over...', True, (255,255,255))
        self.text1 = self.font_results.render(message1, True, (255,255,255))
        self.text2 = self.font_results.render(message2, True, (255,255,255))
        self.text3 = self.font_results.render(message3, True, (255,255,255))
        self.text_rect1 = self.text1.get_rect()
        self.text_rect1.center = (self.HALF_SCREEN_WIDTH-250, self.HALF_SCREEN_HEIGHT-100)
        self.text_rect2 = self.text2.get_rect()
        self.text_rect2.center = (self.HALF_SCREEN_WIDTH-250, self.HALF_SCREEN_HEIGHT+0)
        self.text_rect3 = self.text3.get_rect()
        self.text_rect3.center = (self.HALF_SCREEN_WIDTH-250, self.HALF_SCREEN_HEIGHT+100)
