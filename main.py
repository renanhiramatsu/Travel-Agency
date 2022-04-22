from flask import Flask
from flask_restful import Api
from resources.hotel import Hotels, Hotel


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

# Endpoints
api.add_resource(Hotels, '/hotels')
api.add_resource(Hotel, '/hotels/<int:hotel_id>')


if __name__ == '__main__':
    from sql_alchemy import db
    db.init_app(app)
    app.run(debug=True)