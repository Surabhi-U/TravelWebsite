from flask_login import UserMixin

from db import get_db

class User(UserMixin):
    def __init__(self, id_, email, password):
        self.id = id_
        self.email = email
        self.password = password

    @staticmethod
    def get(user_id):
        db = get_db()
        user = db.execute(
            "SELECT * FROM user WHERE id = ?", (user_id,)
        ).fetchone()
        if not user:
            return None

        user = User(
            id_=user[0], email=user[1], password=user[2]
        )
        return user

    @staticmethod
    def create(id_,email, password):
        db = get_db()
        db.execute(
            "INSERT INTO user (id,email, password) "
            "VALUES (?, ?, ?)",
            (id_,  email, password),
        )
        db.commit()