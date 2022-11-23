from sql_alchemy import db
class HotelModel(db.Model):

    __tablename__ = 'hotels' # This is the name of the table in the database

    hotel_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    city = db.Column(db.String(80))
    stars = db.Column(db.Float(precision=1))
    price = db.Column(db.Float(precision=2))

    def save_to_db(self): # This method is used to save the data to the database
        pass


    def __init__(self, hotel_id, name, city, stars, price):
        self.hotel_id = hotel_id
        self.name = name
        self.city = city
        self.stars = stars
        self.price = price

    def json(self): # This method is used to return the data in a json format
        return {
            'hotel_id': self.hotel_id,
            'name': self.name,
            'city': self.city,
            'stars': self.stars,
            'price': self.price
        }
        
    @classmethod
    def find_hotel(cls, hotel_id):
        return cls.query.filter_by(hotel_id=hotel_id).first() if cls.query.filter_by(hotel_id=hotel_id).first() else None
        # SELECT * FROM hotels WHERE hotel_id = hotel_id

    def save_hotel(self):
        db.session.add(self)
        db.session.commit()

    def update_hotel(self, name, city, stars, price):
        self.name = name
        self.city = city
        self.stars = stars
        self.price = price
        db.session.commit()

    def delete_hotel(self):
        db.session.delete(self)
        db.session.commit()