class Settings():
    """ Class for localizing settings to one place"""

    def __init__(self):
        self.screen_size = (1024, 768)
        self.bg_color = (0, 0, 0)
        self.bullet_speed_factor = 1
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (255, 64, 64)
        self.bullet_limit = 3
        self.alien_speed_factor = .1
        self.fleet_drop_speed = 50
        self.fleet_direction = 1
        self.ship_limit = 2