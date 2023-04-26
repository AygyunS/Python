from typing import List
from project.band_members.musician import Musician


class Band:
    def __init__(self, name: str):
        if not name:
            raise ValueError("Band name should contain at least one character!")
        self.name = name
        self.members = []

    def add_member(self, member: Musician):
        self.members.append(member)

    def __str__(self):
        return f"{self.name} with {len(self.members)} members."
