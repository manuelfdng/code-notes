from flask import Flask
from flask_restful import Api
from config import Config
from models import db
from resources import GunplaListResource, GunplaResource


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize the database with the app
    db.init_app(app)
    with app.app_context():
        db.create_all()

    api = Api(app)
    api.add_resource(GunplaListResource, '/gunplas')
    api.add_resource(GunplaResource, '/gunplas/<int:gunpla_id>')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)