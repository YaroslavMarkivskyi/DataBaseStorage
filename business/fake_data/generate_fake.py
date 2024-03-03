from faker import Faker
import random


class FakerGenerator:
    """
    A class to generate fake data using the faker library.
    """
    def __init__(self):
        self.__fake = Faker()

    def generate_fake_service_type(self):
        """Generate a fake service type."""
        return {
            "name": self.__fake.job()[0:25],
            "description": self.__fake.sentence()[0:100],
            "price": random.randint(100, 10000),
        }

    def generate_fake_visit(self):
        """Generate a fake visit."""
        return {
            "medical_card": random.randint(1, 500),
            "date": self.__fake.date_this_year(),
        }

    def generate_fake_service(self):
        """Generate a fake service."""
        return {
            "doctor_service": random.randint(1, 100),
            "visit": random.randint(1, 500),
            "description": self.__fake.sentence()[0:100],
            "conclusion": self.__fake.sentence()[0:100],
        }

    @staticmethod
    def generate_fake_doctor_service():
        """Generate a fake doctor service."""
        return {
            "service_type": random.randint(1, 20),
            "doctor": random.randint(1, 50),
        }

    def generate_fake_patient(self):
        """Generate a fake patient."""
        fake_patient = {
            "birth_day": self.__fake.date_of_birth(minimum_age=18, maximum_age=65),
            "gender": random.choice([1, 2]),
        }
        fake_user = self.__generate_fake_user()
        return {**fake_user, **fake_patient}

    def generate_fake_doctor(self):
        """Generate a fake doctor."""
        fake_doctor = {
            "education": self.__fake.job()[0:50],
        }
        fake_user = self.__generate_fake_user()
        return {**fake_user, **fake_doctor}

    def __generate_fake_user(self):
        """Generate a fake user."""
        return {
            "first_name": self.__fake.first_name()[0:20],
            "name": self.__fake.last_name()[0:20],
            "last_name": self.__fake.last_name()[0:20],
            "email": self.__fake.email()[0:20],
            "phone": self.__fake.phone_number()[:10],
            "password": self.__fake.password()[0:128],
        }
