from sqlalchemy import Column, Integer, String, Date
from app.database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    date_of_birth = Column(Date, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    phone = Column(String, nullable=True)
    course = Column(String, nullable=True)
    address = Column(String, nullable=True)
    enrollment_date = Column(Date, nullable=True)