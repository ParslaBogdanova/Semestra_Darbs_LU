from OOP.Circle import Circle


class Game():
    def __init__(self):
        self.circle = Circle()
        self.miss_count = 0
        self.max_misses = 10
        self.game_over = False

    def check_miss(self):
        if self.circle.radius <= 0:
            self.miss_count += 1
            self.circle.spawn()
            if self.miss_count >= self.max_misses:
                self.game_over = True

    def restart(self):
        self.miss_count = 0
        self.game_over = False
        self.circle.__init__()
