class HorseRace:
    def __init__(self, race_type: str):
        self.race_type = race_type
        self.jockeys = []

    @property
    def race_type(self):
        return self._race_type

    @race_type.setter
    def race_type(self, value):
        if value not in ["Winter", "Spring", "Autumn", "Summer"]:
            raise ValueError("Race type does not exist!")
        self._race_type = value
