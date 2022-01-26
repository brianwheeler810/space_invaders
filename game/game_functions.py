import sys
from time import sleep
import pygame as pg
from bullet import Bullet
from alien import Alien


def check_events(s, screen, ship, bullets):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            check_keydown_events(event, s, screen, ship, bullets)
        elif event.type == pg.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, s, screen, ship, bullets):
    if event.key == pg.K_RIGHT:
        ship.moveRight = True
    elif event.key == pg.K_LEFT:
        ship.moveLeft = True
    elif event.key == pg.K_SPACE:
        if len(bullets) < s.bullet_limit:
            new_bullet = Bullet(s, screen, ship)
            bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pg.K_RIGHT:
        ship.moveRight = False
    elif event.key == pg.K_LEFT:
        ship.moveLeft = False

def update_screen(settings, screen, ship, aliens, bullets):
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    for alien in aliens.sprites():
        alien.blitme()
    pg.display.flip()

def update_bullets(settings, screen, ship, aliens, bullets):
    bullets.update()
    collisions = pg.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) <= 0:
        bullets.empty()
        create_fleet(settings, screen, ship, aliens)
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def create_fleet(settings, screen, ship, aliens):
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(settings, alien_width)
    number_rows = get_number_rows(settings, ship.rect.height, alien.rect.height)
    for row in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(settings,screen, aliens, alien_number, row)

def get_number_aliens_x(settings, alien_width):
    available_space_x = settings.screen_size[0] - 2 * alien_width
    number_aliens_x = int(available_space_x/(2*alien_width))
    return number_aliens_x

def get_number_rows(settings, ship_height, alien_height):
    available_space_y = settings.screen_size[1] - (8 * alien_height) - ship_height
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows

def create_alien(settings, screen, aliens, alien_number, row_number):
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def check_aliens_bottom(settings, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(settings, stats, screen, ship, aliens, bullets)
            break

def update_aliens(settings, stats, screen, ship, aliens, bullets):
    check_fleet_edges(settings, aliens)
    aliens.update()
    check_aliens_bottom(settings, stats, screen, ship, aliens, bullets)
    if pg.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, stats, screen, ship, aliens, bullets)

def check_fleet_edges(settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break

def change_fleet_direction(settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1

def ship_hit(settings, stats, screen, ship, aliens, bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        aliens.empty()
        bullets.empty()
        create_fleet(settings, screen, ship, aliens)
        sleep(0.5)
        ship.center_ship()
    else:
        stats.active = False



