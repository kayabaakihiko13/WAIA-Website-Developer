from werkzeug.security import generate_password_hash,check_password_hash
from sqlalchemy import Column,Integer,String,Text
from . import db
class Users(db.Model):
    __tablename__="Users"
    id = Column(Integer,primary_key=True)
    firstName = Column(String(100),nullable=False)
    lastName = Column(String(100),nullable=False)
    userName = Column(String(100),unique=True,nullable=False)
    email = Column(String(100),unique=True,nullable=False)
    password = Column(String(128),nullable=False)
    
    def set_password(self,password):
        self.password= generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password,password)

    def __repr__(self) -> str:
        return f"{self.userName} was been Created"
class Note(db.Model):
    id = Column(Integer,primary_key=True)
    text = Column(Text)
    def __repr__(self) -> str:
        return f"the note was been Created"