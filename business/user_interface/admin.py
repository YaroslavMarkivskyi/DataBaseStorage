from business.core.database import Database

from models import (Gender,
                    User,
                    Patient,
                    MedicalCard,
                    Doctor,
                    ServiceType,
                    DoctorService,
                    Visit,
                    Service
                    )


class AdminInterface:
    """
    This class is responsible for providing the admin with the interface to manage the system.
    """
    def __init__(self, db: Database):
        self.__db = db

    def register_patient(self, **kwargs):
        """Register a new user."""
        patient = Patient(
            birth_day=kwargs.get('birth_day'),
            gender=kwargs.get('gender'),
        )
        self.__register_user(patient, **kwargs)
        medical_card = MedicalCard(
            patient=patient.id
        )
        self.__db.add_record(medical_card)

    def register_doctor(self, **kwargs):
        """Register a new doctor."""
        doctor = Doctor(
            education=kwargs.get('education'),
        )
        self.__register_user(doctor, **kwargs)

    def create_service_type(self, **kwargs):
        """Create a new service type."""
        service_type = ServiceType(
            name=kwargs.get('name'),
            description=kwargs.get('description'),
        )
        self.__db.add_record(service_type)

    def create_doctor_service(self, **kwargs):
        """Create a new doctor service."""
        doctor_service = DoctorService(
            service_type=kwargs.get('service_type'),
            doctor=kwargs.get('doctor'),
        )
        self.__db.add_record(doctor_service)

    def create_visit(self, **kwargs):
        """Create a new visit."""
        visit = Visit(
            medical_card=kwargs.get('medical_card'),
            date=kwargs.get('date'),
        )
        self.__db.add_record(visit)

    def create_service(self, **kwargs):
        """Create a new service."""
        service = Service(
            doctor_service=kwargs.get('doctor_service'),
            visit=kwargs.get('visit'),
            description=kwargs.get('description'),
            conclusion=kwargs.get('conclusion'),
        )
        self.__db.add_record(service)

    def create_gender(self, name: str):
        """Add gender to the database."""
        gender = Gender(
            name=name
        )
        self.__db.add_record(gender)

    def __register_user(self, person, **kwargs):
        """Get user model."""
        user = User(
            first_name=kwargs.get('first_name'),
            name=kwargs.get('name'),
            last_name=kwargs.get('last_name'),
            phone=kwargs.get('phone'),
            email=kwargs.get('email'),
            password=kwargs.get('password')
         )
        self.__db.add_record(user)
        person.user = user.id
        self.__db.add_record(person)
