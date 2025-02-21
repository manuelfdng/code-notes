from flask import Flask, send_from_directory
from flask_restful import Api
from config.settings import Config
from app.models import db
import os

def create_app(config_class=Config):
    app = Flask(__name__, static_folder='../../frontend/dist', static_url_path='')
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    
    # Initialize API
    api = Api(app)
    
    # Register blueprints and resources
    from app.api.routes import initialize_routes
    initialize_routes(api)
    
    # Create database tables
    with app.app_context():
        db.create_all()

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve(path):
        if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
            return send_from_directory(app.static_folder, path)
        return send_from_directory(app.static_folder, 'index.html')

    return app