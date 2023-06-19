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
                    self.enemy_bullets.remove(bullet)
                    pygame.time.delay(1000)
                    if game.player.lives < 1:
                        game.playing = False
                    break

                self.enemy_bullets.remove(bullet)

            if len (game.enemy_manager.enemies) > 0:
                for i in range(0,2):
                    if len (game.enemy_manager.enemies) > i and bullet.rect.colliderect(game.enemy_manager.enemies[i].rect) and bullet.owner == 'player':
                        EXPLOSION_SONIDO.play()
                        game.score += 100
                        self.explosion(game,game.enemy_manager.enemies[i])
                        game.enemy_manager.enemies.remove(game.enemy_manager.enemies[i].rect)


        for bullet in self.player_bullets:
            bullet.update(self.player_bullets)

    def explosion(self, game, enemigo):
        x = enemigo.rect.x + (enemigo.rect.width - EXPLOSION_1.get_width()) // 2
        y = enemigo.rect.y + (enemigo.rect.height - EXPLOSION_1.get_height()) // 2

        imagenes_explosion = [EXPLOSION_1, EXPLOSION_2, EXPLOSION_3, EXPLOSION_4, EXPLOSION_5, EXPLOSION_6, EXPLOSION_7, EXPLOSION_8, EXPLOSION_9, EXPLOSION_10, EXPLOSION_11, EXPLOSION_12]

        for i, imagen_explosion in enumerate(imagenes_explosion):
            game.screen.blit(imagen_explosion, (x, y-10))

            pygame.display.flip()



    def draw (self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        for bullet in self.player_bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == "enemy":
                self.enemy_bullets.append(bullet)
        elif bullet.owner == "player":
            self.enemy_bullets.append(bullet)


    def reset(self):
        self.bullets = []
        self.player_bullets = []
        self.enemy_bullets = []