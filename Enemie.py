import random

import pygame
from pygame.math import Vector2

import core


class Enemie:
    def __init__(self,largeur=1000,hauteur=800):
        self.rayon = 20
        self.couleur = (255, 255, 255)
        self.position = Vector2(random.randint(0, largeur),random.randint(0, hauteur))
        self.nom = "Enemie"
        self.vitesse = Vector2(0,0)

    def dead(self):
        self.position = Vector2(random.randint(0, 800), random.randint(0, 800))

    def show(self,screen):
        pygame.draw.circle(screen,self.couleur,self.position,self.rayon)