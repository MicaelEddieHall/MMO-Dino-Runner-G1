from pygame.sprite import Sprite
##si te aparece en blanco despues del import, es que no lo reconoce, seguramente la escritura

import pygame

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING,DEFAULT_TYPE,SHIELD_TYPE,RUNNING_SHIELD,DUCKING_SHIELD,JUMPING_SHIELD,SCREEN_WIDTH,SCREEN_HEIGHT
##RUNNING CTRL+. Y aparecen opciones

JUMP_VELOCITY=8
Y_INITIAL=310
X_INITIAL=80
Y_D_DUCKING=30
S_JUMPING="jumping"
S_RUNNING="running"
S_BEND="bend"

DUCKING_IMG={DEFAULT_TYPE: DUCKING,SHIELD_TYPE : DUCKING_SHIELD}
RUNNING_IMG={DEFAULT_TYPE: RUNNING,SHIELD_TYPE : RUNNING_SHIELD}
JUMPING_IMG={DEFAULT_TYPE: RUNNING,SHIELD_TYPE : JUMPING_SHIELD}

##del update separar cada una de las 3 acciones en 3 metodos
##ademas tomar en cuenta que en el bend debemos actualizar la recta para evitar bugs con los obstaculos


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
        self.y_current=Y_INITIAL
        self.time_to_show=0
        
    
    def run(self):
        self.image=RUNNING_IMG[self.type][self.step//5]
        self.rect=self.image.get_rect()
        self.rect.y=self.y_current
        self.step+=1

    def bend(self):
        self.image=DUCKING_IMG[self.type][self.step//5]
        self.rect=self.image.get_rect()
        self.rect.y=self.y_current+Y_D_DUCKING
        self.step+=1

    def jumping(self):
        self.image=JUMPING
        self.rect.y-=self.jump_velocity*4
        self.y_current=self.rect.y
        self.jump_velocity-=0.8

        
    
    def update(self, user_input):
        if user_input[pygame.K_UP]:
            self.action=S_JUMPING
            self.jumping()
            ##print(self.jump_velocity," ",self.rect.y)
            ##se ejecuta 2 veces por cada pulsacion, no es un error de codigo, sino de mi teclado al pa
            if self.jump_velocity < -JUMP_VELOCITY:
                self.y_current=Y_INITIAL
                self.action=S_RUNNING
                self.jump_velocity=JUMP_VELOCITY
                self.run()
        elif user_input[pygame.K_DOWN]:
            self.action=S_BEND
            self.bend()
        else:
            self.action=S_RUNNING
            self.run()

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
