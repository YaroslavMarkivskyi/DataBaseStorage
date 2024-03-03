from faker import Faker
import random

from models import *


class FakerGenerator:
    """
    A class to generate fake data using the faker library.
    """
    def __init__(self):
        self.__fake = Faker()

    def generate_team(self):
        """Method to generate a team."""
        return Team(
            name=self.__fake.company(),
            stadium=self.__fake.company(),
            coach=self.__fake.name(),
            country=self.__fake.country(),
            city=self.__fake.city()
        )

    def generate_player(self, team_id):
        """Method to generate a player."""
        return Player(
            team=team_id,
            name=self.__fake.name(),
            age=random.randint(18, 40),
            position=self.__fake.job()
        )

    def generate_referee(self):
        """Method to generate a referee."""
        return self.__fake.name()
