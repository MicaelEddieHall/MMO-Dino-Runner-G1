from dino_runner.components.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS
import pygame
class ObstacleManager:
    def __init__(self):
        self.obstacles=[]

    def update(self, game):
        if len(self.obstacles)<=3:
            self.obstacles.append(Cactus(SMALL_CACTUS))
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed,self.obstacles)
            if game.player.rect.colliderect(obstacle.rect):
                ##detecta las colisiones
                pygame.time.delay(900)
                game.playing=False

    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)