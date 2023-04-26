from project.band_members.musician import Musician


class Singer(Musician):
    # list of available types of skills for singers
    available_skills = ['sing high pitch notes', 'sing low pitch notes']

    def learn_new_skill(self, new_skill: str) -> str:
        super().learn_new_skill(new_skill)
        return f"{self.name} learned to {new_skill}."
