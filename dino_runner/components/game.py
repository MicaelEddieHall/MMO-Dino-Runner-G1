import pygame 

from dino_runner.components.score import Score

from dino_runner.components.dinosaur import dinosaur

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, SHIELD

from dino_runner.components.obstaclemanager import ObstacleManager

class Game:
    def __init__(self):


        pygame.init()
        pygame.display.set_caption(TITLE) 
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.runing=False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        
        self.player=dinosaur()
        self.obstacle_manager=ObstacleManager()
        self.score=Score()
        self.dead_count=0

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            if not self.playing:
                self.show_menu()
                
        pygame.quit()

    def play(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset()
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.runing=False

    def update(self):
        user_input=pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self.game_speed,self.player,self.on_death)
        self.score.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
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
        


        #agregar un texto de inicio en la pantalla
        font=pygame.font.Font('freesansbold.ttf',30)
        ##render convierte texto en surface
        text=font.render("Press any key to start.",True,(0,0,0))
        text_rect=text.get_rect()
        text_rect.center=(center_x,center_y)
        self.screen.blit(text,text_rect)
        #agregar una imagen en la pantalla
        self.screen.blit(SHIELD,(center_x-49,center_y-101))
        ##refrescar pantalla
        pygame.display.update()
        #manejar eventos
        self.handle_menu_events()
    
    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runing = False
            elif event.type==pygame.KEYDOWN:
                self.play()

    