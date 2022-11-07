# Unit tests for models.py
#
# Path: test/models/test_models.py

from main.models.user_model import UserModel
from main.models.hotel import HotelModel

class TestUserModel:
    def test_create_user(self):
        user = UserModel('user_id', 'first_name', 'last_name', 'u_login', 'u_password')
        assert user.user_id == 'user_id'
        assert user.first_name == 'first_name'
        assert user.last_name == 'last_name'
        assert user.u_login == 'u_login'
        assert user.u_password == 'u_password'
    
    def test_parse_to_json(self):
        user = UserModel('user_id', 'first_name', 'last_name', 'u_login', 'u_password')
        assert user.parse_to_json() == {
            'user_id' : 'user_id',
            'first_name' : 'first_name',
            'last_name' : 'last_name',
            'u_login' : 'u_login'
        }
    
    def test_find_user(self):
        user = UserModel('user_id', 'first_name', 'last_name', 'u_login', 'u_password')
        assert user.find_user('user_id') == user
    
    def test_save_user(self):
        user = UserModel('user_id', 'first_name', 'last_name', 'u_login', 'u_password')
        user.save_user()
        assert user.find_user('user_id') == user
    
    def test_delete_user(self):
        user = UserModel('user_id', 'first_name', 'last_name', 'u_login', 'u_password')
        user.save_user()
        assert user.find_user('user_id') == user
        user.delete_user()
        assert user.find_user('user_id') == None

class TestHotelModel:
    def test_create_hotel(self):
        hotel = HotelModel('hotel_id', 'name', 'star', 'daily', 'city')
        assert hotel.hotel_id == 'hotel_id'
        assert hotel.name == 'name'
        assert hotel.star == 'star'
        assert hotel.daily == 'daily'
        assert hotel.city == 'city'
    
    def test_parse_to_json(self):
        hotel = HotelModel('hotel_id', 'name', 'star', 'daily', 'city')
        assert hotel.parse_to_json() == {
            'hotel_id' : 'hotel_id',
            'name' : 'name',
            'star' : 'star',
            'daily' : 'daily',
            'city' : 'city'
        }
    
    def test_find_hotel(self):
        hotel = HotelModel('hotel_id', 'name', 'star', 'daily', 'city')
        assert hotel.find_hotel('hotel_id') == hotel
    
    def test_save_hotel(self):
        hotel = HotelModel('hotel_id', 'name', 'star', 'daily', 'city')
        hotel.save_hotel()
        assert hotel.find_hotel('hotel_id') == hotel
    
    def test_delete_hotel(self):
        hotel = HotelModel('hotel_id', 'name', 'star', 'daily', 'city')
        hotel.save_hotel()
        assert hotel.find_hotel('hotel_id') == hotel
        hotel.delete_hotel()
        assert hotel.find_hotel('hotel_id') == None
