from project.band_members.guitarist import Guitarist
from project.band_members.drummer import Drummer
from project.band_members.singer import Singer
from project.band import Band
from project.concert import Concert


class ConcertTrackerApp:
    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in ["Guitarist", "Drummer", "Singer"]:
            raise ValueError("Invalid musician type!")

        for musician in self.musicians:
            if musician.name == name:
                raise Exception(f"{name} is already a musician!")

        musician = None
        if musician_type == "Guitarist":
            musician = Guitarist(name, age)
        elif musician_type == "Drummer":
            musician = Drummer(name, age)
        elif musician_type == "Singer":
            musician = Singer(name, age)

        self.musicians.append(musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        for band in self.bands:
            if band.name == name:
                raise Exception(f"{name} band is already created!")

        band = Band(name)
        self.bands.append(band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for concert in self.concerts:
            if concert.place == place:
                raise Exception(f"{place} is already registered for {concert.genre} concert!")

        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = None
        for m in self.musicians:
            if m.name == musician_name:
                musician = m
                break
        if musician is None:
            raise Exception(f"{musician_name} isn't a musician!")

        band = None
        for b in self.bands:
            if b.name == band_name:
                band = b
                break
        if band is None:
            raise Exception(f"{band_name} isn't a band!")

        band.add_member(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = None
        for b in self.bands:
            if b.name == band_name:
                band = b
                break
        if band is None:
            raise Exception(f"{band_name} isn't a band!")

        musician = None
        for m in band.members:
            if m.name == musician_name:
                musician = m
                break
        if musician is None:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.remove_member(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str) -> str:
        # Check if the band has at least one member of each type
        has_guitarist = False
        has_drummer = False
        has_singer = False
        for band in self.bands:
            if band.name == band_name:
                for member in band.members:
                    if isinstance(member, Guitarist):
                        has_guitarist = True
                    elif isinstance(member, Drummer):
                        has_drummer = True
                    elif isinstance(member, Singer):
                        has_singer = True
        if not has_guitarist or not has_drummer or not has_singer:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        # Find the concert and band objects
        concert = None
        for c in self.concerts:
            if c.place == concert_place:
                concert = c
                break
        if concert is None:
            raise Exception(f"No concert found in {concert_place}!")

        band = None
        for b in self.bands:
            if b.name == band_name:
                band = b
                break
        if band is None:
            raise Exception(f"No band found with name {band_name}!")

        # Check if the band has the required skills to play at the concert
        if concert.genre == "Rock":
            for member in band.members:
                if isinstance(member, Guitarist) and not member.can_play_rock():
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif isinstance(member, Drummer) and not member.can_play_drums_with_sticks():
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif isinstance(member, Singer) and not member.can_sing_high_notes():
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
        elif concert.genre == "Metal":
            for member in band.members:
                if isinstance(member, Guitarist) and not member.can_play_metal():
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif isinstance(member, Drummer) and not member.can_play_drums_with_sticks():
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif isinstance(member, Singer) and not member.can_sing_low_notes():
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
        elif concert.genre == "Jazz":
            for member in band.members:
                if isinstance(member, Guitarist) and not member.can_play_jazz():
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif isinstance(member, Drummer) and not member.can_play_drums_with_brushes():
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif isinstance(member, Singer) and not (member.can_sing_high_notes() and member.can_sing_low_notes()):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = round((concert.audience * concert.ticket_price) - concert.expenses, 2)
        band.earn_profit(profit)

        return f"{band_name} gained {profit}$ from the {concert.genre} concert in {concert_place}."

