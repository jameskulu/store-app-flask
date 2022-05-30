from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api

from app.resources.item import Item, ItemList
from app.resources.store import Store, StoreList
from app.resources.user import Register, Login
from app.config import postgresqlConfig

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = postgresqlConfig
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config["JWT_SECRET_KEY"] = "asdajjk3b43kjb4k34b"
jwt = JWTManager(app)
api = Api(app)


@app.before_first_request
def create_tables():
    from app.db import db
    db.init_app(app)
    db.create_all()


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':
    app.run(debug=True)