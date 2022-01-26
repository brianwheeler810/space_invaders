class Stats():
    def __init__(self, settings):
        self.settings = settings
        self.reset_stats()
        self.active = True


    def reset_stats(self):
        self.ships_left = self.settings.ship_limit - 1