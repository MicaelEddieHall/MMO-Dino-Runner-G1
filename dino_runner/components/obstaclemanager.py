from dino_runner.components.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS
import pygame
import random

class ObstacleManager:
    def __init__(self):
        self.obstacles=[]
        self.list_cactus=[SMALL_CACTUS,LARGE_CACTUS]
        self.list_tall=[325,300]
        self.cactus=0
        self.Cactus=Cactus(SMALL_CACTUS)

    def update(self, game_speed,player,on_death):
        if len(self.obstacles)<1:
            self.cactus=random.randint(0,1)
            self.Cactus=Cactus(self.list_cactus[self.cactus])
            self.Cactus.rect.y=self.list_tall[self.cactus]
            self.obstacles.append(self.Cactus)
        for obstacle in self.obstacles:
            obstacle.update(game_speed,self.obstacles)
            if player.rect.colliderect(obstacle.rect):
                ##detecta las colisiones
                on_death(self)

    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
    def reset(self):
        self.obstacles=[]