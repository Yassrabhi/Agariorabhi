import random

from pygame.math import Vector2


class Carte:
    def __init__(self,largeur=1000,hauteur=800):
        self.taille = Vector2(1000,800)
        self.couleur = (random.randint(0, 255) ,random.randint(0, 255) ,random.randint(0, 255))
        self.fps = 3


