from dino_runner.components.power_ups.power_up import PowerUp

from dino_runner.components.power_ups.shield import Shield

from dino_runner.components.power_ups.Hammer import Hammer

import pygame

import random

class PowerUpManager:
    def __init__(self):
        self.power_ups: list[PowerUp]=[]
        self.when_appears=0

    def generate_power_up(self,score):
        power=[Shield(),Hammer()]
        ##ve si tiene al menos 1 elemento
        if not self.power_ups and self.when_appears==score:
            self.when_appears+=random.randint(300,400)
            ##aca debo cambiar eso por un random.choise() xd
            self.power_ups.append(power[random.randint(0,1)])
            

    def update(self, game_speed,score,player):
        self.generate_power_up(score)
        for power_up in self.power_ups:
            power_up.update(game_speed,self.power_ups)
            if power_up.rect.colliderect(player.rect):
                power_up.start_time=pygame.time.get_ticks()
                player.on_pick_power_up(power_up)
                self.power_ups.remove(power_up)
                break

    def draw(self,screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
    
    def reset(self):
        self.power_ups=[]
        self.when_appears=random.randint(200,300)
