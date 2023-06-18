import pygame

from game.utils.constants import EXPLOSION_1, EXPLOSION_10, EXPLOSION_11, EXPLOSION_12, EXPLOSION_2, EXPLOSION_3, EXPLOSION_4, EXPLOSION_5, EXPLOSION_6, EXPLOSION_7, EXPLOSION_8, EXPLOSION_9, EXPLOSION_SONIDO, SHIELD_TYPE


class BulletManager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []
        self.player_bullets = []

    def update (self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                if game.player.power_up_type != SHIELD_TYPE:
                    game.death_count += 1
                    game.lives_count += 1
                    game.player.subtract_lives(game.screen)
                    pygame.time.delay(1000)
                    if game.player.lives < 1:
                        game.playing = False
                    break

                self.enemy_bullets.remove(bullet)

            if len (game.enemy_manager.enemies) > 0:
                if bullet.rect.colliderect(game.enemy_manager.enemies[0].rect) and bullet.owner == 'player':
                    EXPLOSION_SONIDO.play()
                    game.score += 100
                    game.score_total += 100
                    self.explosion(game,game.enemy_manager.enemies[0])
                    game.enemy_manager.enemies = []

                    
        for bullet in self.player_bullets:
            bullet.update(self.player_bullets)

    def explosion(self, game, enemigo):
        x = enemigo.rect.x + (enemigo.rect.width - EXPLOSION_1.get_width()) // 2
        y = enemigo.rect.y + (enemigo.rect.height - EXPLOSION_1.get_height()) // 2

        imagenes_explosion = [EXPLOSION_1, EXPLOSION_2, EXPLOSION_3, EXPLOSION_4, EXPLOSION_5, EXPLOSION_6, EXPLOSION_7, EXPLOSION_8, EXPLOSION_9, EXPLOSION_10, EXPLOSION_11, EXPLOSION_12]

        for i, imagen_explosion in enumerate(imagenes_explosion):
            game.screen.blit(imagen_explosion, (x, y-10))

            pygame.display.flip()
            """ pygame.time.wait(1000)"""



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

    def reset(self):
        self.bullets = []
        self.enemy_bullets = []