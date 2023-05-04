import pygame
class Score:
    def __init__(self):
        self.score=0
    
    def update(self,game):
        self.score+=1
        if self.score%100==0:
            game.game_speed+=1
    
    def draw(self,screen):
        font=pygame.font.Font('freesansbold.ttf',22)
        ##render convierte texto en surface
        text=font.render(f"Score: {self.score}",True,(0,0,0))
        text_rect=text.get_rect()
        text_rect.center=(1000,50)
        screen.blit(text,text_rect)

    def reset(self):
        self.score=0
        