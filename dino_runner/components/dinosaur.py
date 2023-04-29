from pygame.sprite import Sprite
##si te aparece en blanco despues del import, es que no lo reconoce, seguramente la escritura

import pygame

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING
##RUNNING CTRL+. Y aparecen opciones

JUMP_VELOCITY=8.5
Y_INITIAL=310
X_INITIAL=80

##esta heredando sprite a dinosaur
class dinosaur(Sprite):
    def __init__(self):
        self.image=RUNNING[0]
        self.rect=self.image.get_rect()
        self.rect.x=X_INITIAL##izquierda a derecha
        self.rect.y=Y_INITIAL##arriba hacia abajo se cuenta

        self.step=0
        self.action="running"
        self.jump_velocity=JUMP_VELOCITY

    def update(self, user_input):
        if self.action=="running":
            self.image=RUNNING[0] if self.step < 5 else RUNNING[1]
            self.step+=1
        elif self.action=="jumping":
            self.image=JUMPING
            self.rect.y-=self.jump_velocity*4
            self.jump_velocity -=0.8
            
            if self.jump_velocity < -JUMP_VELOCITY:
                self.rect.y=Y_INITIAL
                self.action="running"
                self.jump_velocity=JUMP_VELOCITY
        elif self.action=="bend":
            self.image=DUCKING[0] if self.step < 5 else DUCKING[1]
            self.step+=1
            if self.step==9 and not user_input[pygame.K_DOWN]:
                self.image=RUNNING[0] if self.step < 5 else RUNNING[1]
                self.action="running"

        if user_input[pygame.K_UP] and self.action!="jumping":
            self.action="jumping"
        elif self.action=="jumping":
            self.action="running"
        elif user_input[pygame.K_DOWN]:
            self.action="bend"
            ##cada vez que termina de hacer un salto, se vuelve a poner a correr en el aire xd
        
        if self.step>=10:
            self.step=0



    def draw(self, screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))##cada blit es una capa de dibujo


