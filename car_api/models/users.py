from sqlalchemy import Column, Integer, String, DateTime, func

from car_api.models import Base


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    updated_at = Column(
        DateTime, 
        server_default=func.now(),
        onupdate=func.now()
    )
    created_at = Column(
        DateTime,
        server_default=func.now()
    )
