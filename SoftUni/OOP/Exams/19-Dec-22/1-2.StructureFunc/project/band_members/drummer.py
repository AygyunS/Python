from project.band_members.musician import Musician



class Drummer(Musician):
    # list of available types of skills for drummers
    available_skills = ['play the drums with drumsticks', 'play the drums with drum brushes', 'read sheet music']

    def learn_new_skill(self, new_skill: str) -> str:
        super().learn_new_skill(new_skill)
        return f"{self.name} learned to {new_skill}."
