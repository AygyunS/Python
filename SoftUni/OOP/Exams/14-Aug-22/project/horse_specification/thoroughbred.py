from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    max_speed = 140

    def train(self):
        self.speed = min(self.speed + 3, self.max_speed)
