from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Hotels(Resource):
    def get(self):
        return {
            'hotels': ['Marriot', 'Hilton', 'Holiday Inn', "Wyndham"]
        }

