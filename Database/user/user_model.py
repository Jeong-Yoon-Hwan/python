from Database.postgres import session, base
from sqlalchemy import Column, String, Boolean, Integer, Float, DateTime, Sequence

class User(base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)    
    username = Column(String)                        
    password = Column(String)                        


def get_users():
    users = session.query(User).all()
    
    userData = list()
    
    for data in users:
        userData.append(data)
    
    print(userData)

def get_user(data):
    user = session.query(User).filter_by(username = data).first()
    return user