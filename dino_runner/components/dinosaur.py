from pygame.sprite import Sprite
##si te aparece en blanco despues del import, es que no lo reconoce, seguramente la escritura

import pygame

from dino_runner.utils.constants import RUNNING, JUMPING
##RUNNING CTRL+. Y aparecen opciones


##esta heredando sprite a dinosaur
class dinosaur(Sprite):
    def __init__(self):
        self.image=RUNNING[0]
        self.rect=self.image.get_rect()
        self.rect.x=80##izquierda a derecha
        self.rect.y=310##arriba hacia abajo se cuenta

        self.step=0
        self.action="running"
        self.jump_velocity=8.5

    def update(self, user_input):
        if self.action=="running":
            self.image=RUNNING[0] if self.step < 5 else RUNNING[1]
            self.step+=1
        elif self.action=="jumping":
            self.image=JUMPING
            self.rect.y-=self.jump_velocity*4
            self.jump_velocity -=0.8
            
            if self.jump_velocity < -8.5:
                self.rect.y=310
                self.action="running"
                self.jump_velocity=8.5

        if user_input[pygame.K_UP] and self.action!="jumping":
            self.action="jumping"
        elif self.action=="jumping":
            self.action="running"
        
        if self.step>=10:
            self.step=0

    def draw(self, screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))##cada blit es una capa de dibujo


