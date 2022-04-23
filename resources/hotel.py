from flask_restful import Resource, reqparse
from models.hotel import HotelModel

class Hotels(Resource):
    def get(self):
        return {'hotels': [hotel.json() for hotel in HotelModel.query.all()]}
class Hotel(Resource):

    params = reqparse.RequestParser()
    params.add_argument('name', type=str, required=True, help='Name cannot be blank')
    params.add_argument('city', type=str, required=True, help='City cannot be blank')
    params.add_argument('stars', type=float, required=True, help='Stars cannot be blank')
    params.add_argument('price', type=float, required=True, help='Price cannot be blank')


    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json(), 200
        else:
            return {'message': 'Hotel not found'}, 404
        
    
    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {'message': 'Hotel id {} already exists'.format(hotel_id)}, 400

        data = Hotel.params.parse_args()
        new_hotel = HotelModel(hotel_id, **data)

        try: 
            new_hotel.save_hotel()
            return new_hotel.json(), 201
        except:
            return {'message': 'An error occurred while creating the hotel'}, 500
        
        return new_hotel.json(), 201


    def put(self, hotel_id):

        data = Hotel.params.parse_args()
        hotel_isFound = HotelModel.find_hotel(hotel_id)

        if hotel_isFound:
            hotel_isFound.update_hotel(**data)
            hotel_isFound.save_hotel()
            return hotel_isFound.json(), 200
        
        
        new_hotel = HotelModel(hotel_id, **data)
        try:
            new_hotel.save_hotel()
            return new_hotel.json(), 201
        except:
            return {'message': 'An error occurred while creating the hotel'}, 500


    def delete(self, hotel_id):
        
        hotel_isFound = HotelModel.find_hotel(hotel_id)
        if hotel_isFound:
            hotel_isFound.delete_hotel()
            return {'message': 'Hotel deleted'}, 200
        else:
            return {'message': 'Hotel not found'}, 404
        

