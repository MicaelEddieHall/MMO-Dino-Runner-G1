from dino_runner.utils.constants import SCREEN_WIDTH

import pygame

class obstacles:
    def __init__(self,image:pygame.Surface,type):
        self.image=image
        self.type=type
        self.rect=self.image[self.type].get_rect()
        self.rect.x=SCREEN_WIDTH

    def update(self, game_speed, obstacles):
        self.rect.x-=game_speed
        if self.rect.x<-self.rect.width:
            obstacles.pop()


    def draw(self,screen):
        screen.blit(self.image[self.type],self.rect)
