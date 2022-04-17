from flask_restful import Resource, reqparse
from models.hotel import HotelModel

hotels = [{
    'hotel_id': 1,
    'name': 'Marriot',
    'city': 'Cancun',
    'stars': 5,
    'price': 119.29
}, {
    'hotel_id': 2,
    'name': 'Hilton',
    'city': 'Istanbul',
    'stars': 4.2,
    'price': 89.99
}, {
    'hotel_id': 3,
    'name': 'Holiday Inn',
    'city': 'London',
    'stars': 3.9,
    'price': 99.99
}]



class Hotels(Resource):
    def get(self):
        return {
            'hotels': hotels
        }

class Hotel(Resource):

    params = reqparse.RequestParser()
    params.add_argument('name', type=str, required=True, help='Name cannot be blank')
    params.add_argument('city', type=str, required=True, help='City cannot be blank')
    params.add_argument('stars', type=float, required=True, help='Stars cannot be blank')
    params.add_argument('price', type=float, required=True, help='Price cannot be blank')


    def find_hotel(hotel_id):
        for hotel in hotels:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None

    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel, 200
        else:
            return {'message': 'Hotel not found'}, 404
        
    
    def post(self, hotel_id):

        data = Hotel.params.parse_args()

        new_hotel = HotelModel(hotel_id, **data)
        hotels.append(new_hotel.json())
        return new_hotel.json(), 201


    def put(self, hotel_id):

        data = Hotel.params.parse_args()
        new_hotel = HotelModel(hotel_id, **data)

        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hotel.update(new_hotel.json())
            return hotel, 200
        else:
            hotels.append(new_hotel.json())
            return new_hotel.json(), 201


    def delete(self, hotel_id):
        global hotels
        hotels = list(filter(lambda hotel: hotel['hotel_id'] != hotel_id, hotels))
        return {'message': 'Hotel deleted'}, 200

