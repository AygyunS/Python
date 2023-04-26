class Musician:
    # list of available types of skills
    available_skills = ['piano', 'guitar', 'drums', 'bass', 'vocals']

    def __init__(self, name: str, age: int):
        self._name = None
        self._age = None
        self._skills = []

        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Musician name cannot be empty!")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value: int):
        if value < 16:
            raise ValueError("Musicians should be at least 16 years old!")
        self._age = value

    @property
    def skills(self):
        return self._skills

    def learn_new_skill(self, new_skill: str) -> str:
        if new_skill not in self.available_skills:
            raise ValueError(f"{new_skill} is not a needed skill!")
        if new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")
        self.skills.append(new_skill)
        return f"{self.name} learned to {new_skill}."

    def play_solo(self):
        raise NotImplementedError("play_solo() method not implemented for this musician")
