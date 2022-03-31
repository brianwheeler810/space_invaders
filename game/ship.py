import pygame as pg

class Ship():
    def __init__(self, screen):
        self.screen = screen
        self.image = pg.image.load("art/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moveRight = False
        self.moveLeft = False

    def update(self):
        if self.moveRight and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.moveLeft and self.rect.left > 0:
            self.rect.centerx -= 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.centerx = self.screen_rect.centerx
