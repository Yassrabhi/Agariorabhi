import pygame

import core
from Enemie import Enemie
from creep import Creep
from joueur import Joueur





def setup():
    print("Setup START----------")

    core.fps = 30
    core.WINDOW_SIZE = [800, 800]
    core.memory("Creep",Creep())
    core.memory("Joueur", Joueur())
    core.memory("listCreep", [])
    core.memory("listJoueur", [])
    core.memory("ListEnemie", [])


    for c in range(100):
        core.memory("listCreep").append(Creep())
    for j in range(1):
        core.memory("listJoueur").append(Joueur())
    for e in range(5):
        core.memory("ListEnemie").append(Enemie())

def run():

    core.cleanScreen()

#####//// grossir le joueur et faire disparaitre les creeps

    for c in core.memory("listCreep"):
        c.show(core.screen)

    core.memory("Joueur").draw(core.screen)
    core.memory("Joueur").deplacer(core.getMouseLeftClick())

    for c in core.memory("listCreep"):
        if c.position.distance_to(core.memory("Joueur").position) < core.memory("Joueur").rayon + c.rayon :
            c.dead()
            core.memory("Joueur").grossir()

#####//// grossir le joueur et faire disparaitre les ennemies

    for c in core.memory("ListEnemie"):
        c.show(core.screen)

    for c in core.memory("ListEnemie"):
        if c.position.distance_to(core.memory("Joueur").position) < core.memory("Joueur").rayon + c.rayon :
            c.dead()
            core.memory("Joueur").grossir()





core.main(setup, run)