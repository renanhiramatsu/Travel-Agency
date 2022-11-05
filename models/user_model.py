from sql_alchemy import db

class UserModel(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))

    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

    def parseToJson(self):
        return {
            'user_id' : self.user_id,
            'first_name' : self.first_name,
            'last_name' : self.last_name
        }

    @classmethod
    def find_user(cls, user_id):
        return cls.query.filter_by(user_id=user_id).first() if cls.query.filter_by(user_id=user_id).first() else None
    
    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()
    