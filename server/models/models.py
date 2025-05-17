from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):

    __tablename__ = "Users"

    uid = Column(Integer, primary_key=True, autoincrement=True, index=True, unique=True)
    user_name = Column(String, unique=False, nullable=False)
    user_email = Column(String, index=True, unique=True, nullable=False)
    createdOn = Column(DateTime, default=datetime.now, nullable=False)
    updatedOn = Column(DateTime, default=datetime.now, nullable=False)

    def touch(self):
        self.updatedOn = datetime.now()


