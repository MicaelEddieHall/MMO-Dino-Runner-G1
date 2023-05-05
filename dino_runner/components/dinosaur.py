from pygame.sprite import Sprite
##si te aparece en blanco despues del import, es que no lo reconoce, seguramente la escritura

import pygame

from dino_runner.utils.constants import HAMMER_TYPE, HEART_TYPE, RUNNING, JUMPING, DUCKING,DEFAULT_TYPE,SHIELD_TYPE,RUNNING_SHIELD,DUCKING_SHIELD,JUMPING_SHIELD,SCREEN_WIDTH,SCREEN_HEIGHT,DUCKING_HAMMER,JUMPING_HAMMER,RUNNING_HAMMER
##RUNNING CTRL+. Y aparecen opciones

JUMP_VELOCITY=8.5
Y_INITIAL=310
X_INITIAL=80
Y_D_DUCKING=30
S_JUMPING="jumping"
S_RUNNING="running"
S_BEND="bend"

DUCKING_IMG={DEFAULT_TYPE: DUCKING,SHIELD_TYPE : DUCKING_SHIELD,HAMMER_TYPE:DUCKING_HAMMER,HEART_TYPE:DUCKING}
RUNNING_IMG={DEFAULT_TYPE: RUNNING,SHIELD_TYPE : RUNNING_SHIELD,HAMMER_TYPE:RUNNING_HAMMER,HEART_TYPE:RUNNING}
JUMPING_IMG={DEFAULT_TYPE: RUNNING,SHIELD_TYPE : JUMPING_SHIELD,HAMMER_TYPE:JUMPING_HAMMER,HEART_TYPE:RUNNING}



##esta heredando sprite a dinosaur
class dinosaur(Sprite):
    def __init__(self):
        self.type=DEFAULT_TYPE
        self.image=RUNNING_IMG[self.type][0]
        self.rect=self.image.get_rect()
        self.rect.x=X_INITIAL##izquierda a derecha
        self.rect.y=Y_INITIAL##arriba hacia abajo se cuenta

        self.step=0
        self.action=S_RUNNING
        self.jump_velocity=JUMP_VELOCITY
        self.d_ducking=True
        self.time_to_show=0
        self.y_current=Y_INITIAL
        
    
    def run(self):
        self.image=RUNNING_IMG[self.type][self.step//5]
        self.rect=self.image.get_rect()
        self.rect.y=Y_INITIAL
        self.y_current=self.rect.y
        self.jump_velocity=JUMP_VELOCITY
        self.step+=1

    def bend(self):
        self.image=DUCKING_IMG[self.type][self.step//5]
        self.rect=self.image.get_rect()
        self.rect.y=self.y_current+Y_D_DUCKING
        self.step+=1

    def jumping(self):
        self.image=JUMPING
        self.y_current-=self.jump_velocity*4
        self.rect.y=self.y_current
        self.jump_velocity-=0.8
        if  self.jump_velocity<-JUMP_VELOCITY:
            self.rect.y=Y_INITIAL
            self.y_current=Y_INITIAL
            self.action=S_RUNNING
            self.jump_velocity=JUMP_VELOCITY
        
    
    def update(self, user_input):
        if self.action==S_JUMPING:
            self.jumping()
        elif self.action==S_BEND:
            self.bend()
        elif self.action==S_RUNNING:
            self.run()

        if user_input[pygame.K_UP] or self.action==S_JUMPING:
            self.action=S_JUMPING    
        elif user_input[pygame.K_DOWN]:
            self.action=S_BEND
        else:
            self.action=S_RUNNING
        
        

        self.rect.x=X_INITIAL

        if self.step>=10:
            self.step=0

    
    def draw(self, screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))##cada blit es una capa de dibujo

    def on_pick_power_up(self,power_up):
        self.type=power_up.type
        self.power_up_time_up=power_up.start_time + (power_up.duration*1000)


    def draw_power_up(self,screen):
        if self.type!=DEFAULT_TYPE:
            self.time_to_show=round((self.power_up_time_up-pygame.time.get_ticks())/1000,2)
        if self.time_to_show>0:
            ##funcino de mensaje
            self.dibuja_texto(screen,f"{self.type.capitalize()} enable for {self.time_to_show} seconds",SCREEN_WIDTH//2,50)
            ##posicion 50 en y, en x es el centro
        else:
            self.type=DEFAULT_TYPE
            self.power_up_time_up=0

            
    def dibuja_texto(self,screen,texto,center_x,center_y):
        font=pygame.font.Font('freesansbold.ttf',30)
        ##render convierte texto en surface
        text=font.render(texto,True,(0,0,0))
        text_rect=text.get_rect()
        text_rect.center=(center_x,center_y)
        screen.blit(text,text_rect)
