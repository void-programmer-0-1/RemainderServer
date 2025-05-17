from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):

    __tablename__ = "Users"

    uid = Column(Integer, primary_key=True, autoincrement=True, index=True, unique=True)
    user_name = Column(String, unique=False, nullable=False)
    user_email = Column(String, index=True, unique=True, nullable=False)
    user_password = Column(String, nullable=False)
    created_on = Column(DateTime, default=datetime.now, nullable=False)
    updated_on = Column(DateTime, default=datetime.now, nullable=False)

    def touch(self):
        self.updated_on = datetime.now()

    def to_dict(self):
        return {
            "uid": self.uid,
            "user_name": self.user_name,
            "user_email": self.user_email,
            "created_on": self.created_on,
            "updated_on": self.updated_on
        }