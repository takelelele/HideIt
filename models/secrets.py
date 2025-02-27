from sqlalchemy import String, Column
from database import Base

class SecretsModel(Base):
    __tablename__ = 'secrets'

    id = Column(String, primary_key=True, index=True)
    secret = Column(String)
    passphrase = Column(String)