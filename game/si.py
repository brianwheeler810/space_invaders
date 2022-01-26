import pygame as pg
import sys
import time
import random
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from stats import Stats
from pygame.sprite import Group

def si():

    pg.init()
    s = Settings()
    screen = pg.display.set_mode(s.screen_size)
    pg.display.set_caption("Space Invaders")
    stats = Stats(s)
    ship = Ship(screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(s, screen, ship, aliens)

    while True:
        gf.check_events(s, screen, ship, bullets)
        if stats.active:
            ship.update()
            gf.update_bullets(s, screen, ship, aliens, bullets)
            gf.update_aliens(s, stats, screen, ship, aliens, bullets)
        gf.update_screen(s, screen, ship, aliens, bullets)


if __name__ == "__main__":
    si()
