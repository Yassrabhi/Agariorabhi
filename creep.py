import random

import random
import pygame
from pygame.math import Vector2


class Creep:
    def __init__(self):
        self.position = Vector2(random.randint(0,800),random.randint(0,800))
        self.rayon = 5
        self.couleur = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.masse = 10


    def show(self,screen):
        pygame.draw.circle(screen,self.couleur,self.position,self.rayon)

    def dead(self):
        self.position = Vector2(random.randint(0, 800), random.randint(0, 800))
