import pygame

from game.utils.constants import EXPLOSION_SONIDO


class BulletManager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []
        self.player_bullets = []

    def update (self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                self.enemy_bullets.remove(bullet)
                game.playing = False
                pygame.time.delay(1000)
                break

            if len (game.enemy_manager.enemies) > 0:
                if bullet.rect.colliderect(game.enemy_manager.enemies[0].rect) and bullet.owner == 'player':
                    game.enemy_manager.enemies = []
                    EXPLOSION_SONIDO.play()
                    
        for bullet in self.player_bullets:
            bullet.update(self.player_bullets)



    def draw (self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        for bullet in self.player_bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == 'enemy' and len (self.enemy_bullets)<1:
            self.enemy_bullets.append(bullet)
        if bullet.owner == 'player' and len (self.player_bullets)<1:
            self.enemy_bullets.append(bullet)