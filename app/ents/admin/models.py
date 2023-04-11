from sqlalchemy import Column, Integer, String

from app.ents.base.crud import db


class Admin(db.Model):  # type: ignore
    """Admins Table"""

    __tablename__ = "admins"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    username = Column(String)
    password = Column(String)
    role = Column(String)

    def __init__(self, email: str, username: str, password: str, role: str) -> None:
        self.email = email
        self.username = username
        self.password = password
        self.role = role
