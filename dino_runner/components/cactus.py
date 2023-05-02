import random
from dino_runner.components.obstacles import obstacles
class Cactus(obstacles):
    def __init__ (self,image):
        self.type=random.randint(0,2)
        self.image=image[self.type]
        super().__init__(image,self.type)

