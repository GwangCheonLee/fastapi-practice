from config.database import Session
from models.user import User


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def add_user(self, user):
        self.session.add(user)
        self.session.commit()

    def get_user_by_id(self, user_id):
        return self.session.query(User).filter(User.id == user_id).one()

    def get_all_users(self):
        return self.session.query(User).all()
