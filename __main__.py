from business.core.database import Database
from business.core.config import Config
from business.user_interface.admin import AdminInterface
from business.fake_data.generate_fake import FakerGenerator
import random


if __name__ == "__main__":
    db = Database(
        db_type=Config.DB_TYPE,
        db_host=Config.DB_HOST,
        db_name=Config.DB_NAME,
        db_user=Config.DB_USER,
        db_password=Config.DB_PASS
    )

    admin = AdminInterface(db)
    fake = FakerGenerator()

    admin.create_gender("male")
    admin.create_gender("female")
    for _ in range(500):
        admin.register_patient(**fake.generate_fake_patient())
    for _ in range(50):
        admin.register_doctor(**fake.generate_fake_doctor())
    for _ in range(20):
        admin.create_service_type(**fake.generate_fake_service_type())
    for _ in range(100):
        admin.create_doctor_service(**fake.generate_fake_doctor_service())
    for _ in range(5000):
        admin.create_visit(**fake.generate_fake_visit())
    for _ in range(5000):
        number = random.randint(1, 5)
        for _ in range(number):
            admin.create_service(**fake.generate_fake_service())
