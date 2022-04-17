class HotelModel:
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