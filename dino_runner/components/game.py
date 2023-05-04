import pygame 

from dino_runner.components.score import Score

from dino_runner.components.dinosaur import dinosaur


from dino_runner.components.power_ups.powerupmanager import PowerUpManager

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DINO_START

from dino_runner.components.obstaclemanager import ObstacleManager


class Game:
    def __init__(self):


        pygame.init()
        pygame.display.set_caption(TITLE) 
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running=False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        
        self.player=dinosaur()
        self.obstacle_manager=ObstacleManager()
        self.score=Score()
        self.dead_count=0
        self.max_score=0
        self.power_up_manager=PowerUpManager()

    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
            else:
                self.play()
                
        pygame.quit()

    def play(self):
        # Game loop: events - update - draw
        self.reset_game()
        while self.playing:
            self.events()
            self.update()
            self.draw()
        ##doble pygame.quit() genera un self.screen.fill
        ##pygame.quit()
    def reset_game(self):
        self.playing = True
        self.obstacle_manager.reset()
        self.score.reset()
        self.power_up_manager.reset()
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running=False

    def update(self):
        user_input=pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self.game_speed,self.player,self.on_death)
        self.score.update(self)
        self.power_up_manager.update(self.game_speed,self.score.score,self.player)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def on_death(self):
        pygame.time.delay(900)
        self.playing=False
        self.dead_count+=1

    def show_menu(self):
        center_x=SCREEN_WIDTH//2
        center_y=SCREEN_HEIGHT//2
        ##cambiar el fondo de pantalla
        self.screen.fill((255,255,255))

        ##si no hubo muertes mostrar normal, sino mostrar el contador de muertes
        ##mostrar mensaje de reinicio
        ##mostrar puntaje obtenido, al parecer las 3 en una misma ventana
        ##abstraer el codigo de generar texto en medio, para que nos pregunte donde y en que tamaño dibujar
        
        if self.dead_count!=0:
            self.dibuja_texto(f"{self.dead_count}",center_x,center_y+50)

            if self.max_score<self.score.score:
                self.max_score=self.score.score
            self.dibuja_texto(f"max score: {self.max_score}",center_x,center_y+100)
            self.dibuja_texto(f"death count: {self.dead_count}",center_x,center_y+150)
            #agregar un texto de inicio en la pantalla
            ##font=pygame.font.Font('freesansbold.ttf',30)
            ##render convierte texto en surface
            ##text=font.render(f"{self.dead_count}",True,(0,0,0))
            ##text_rect=text.get_rect()
            ##text_rect.center=(center_x,center_y)
            ##self.screen.blit(text,text_rect)

            ##aca usa el dibujar texto 2 veces 
        self.dibuja_texto("Press any key to start",center_x,center_y+50)


            #agregar una imagen en la pantalla

        self.screen.blit(DINO_START,(center_x-49,center_y-121))            
        ##desde la 115 hasta la 122 hacerlo en funcion, y pasar el mensaje de press any key 
        ##refrescar pantalla
        pygame.display.update()
        #manejar eventos
        self.handle_menu_events()
        
    
    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.play()
            elif event.type==pygame.QUIT:
                self.running=False

    def dibuja_texto(self,texto,center_x,center_y):
        font=pygame.font.Font('freesansbold.ttf',30)
        ##render convierte texto en surface
        text=font.render(texto,True,(0,0,0))
        text_rect=text.get_rect()
        text_rect.center=(center_x,center_y)
        self.screen.blit(text,text_rect)

    