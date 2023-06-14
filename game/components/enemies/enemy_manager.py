import random
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1,ENEMY_2

class EnemyManager:
    IMAGES =[ENEMY_2,ENEMY_1]

    def __init__(self):
        self.enemies = []

    def update(self):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies)

    def draw(self,screen):
        for enemy in self.enemies:
            enemy.draw(screen)


    def add_enemy(self):
        if len(self.enemies) <= 0:
            enemy = Enemy(self.IMAGES[random.randint(0,1)])
            self.enemies.append(enemy)