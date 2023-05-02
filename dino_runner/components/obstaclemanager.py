from dino_runner.components.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS
import pygame
import random
class ObstacleManager:
    def __init__(self):
        self.obstacles=[]
        self.list_cactus=[SMALL_CACTUS,LARGE_CACTUS]
        self.list_tall=[325,310]
        self.cactus=0
        self.Cactus=Cactus(SMALL_CACTUS)

    def update(self, game):
        if len(self.obstacles)<=3:
            self.cactus=random.randint(0,1)
            self.Cactus=Cactus(self.list_cactus[self.cactus])
            self.Cactus.rect.y=self.list_tall[self.cactus]
            self.obstacles.append(self.Cactus)
            ##print(len(self.obstacles))
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed,self.obstacles)
            if(obstacle.rect.x<0):
                self.obstacles.pop()
            ##print(obstacle.rect.x)
            ##print("se actualizan")
            if game.player.rect.colliderect(obstacle.rect):
                ##detecta las colisiones
                pygame.time.delay(900)
                game.playing=False

    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)