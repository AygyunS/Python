from project.band_members.musician import Musician


class Guitarist(Musician):
    # list of available types of skills for guitarists
    available_skills = ['play metal', 'play rock', 'play jazz']

    def learn_new_skill(self, new_skill: str) -> str:
        super().learn_new_skill(new_skill)
        return f"{self.name} learned to {new_skill}."