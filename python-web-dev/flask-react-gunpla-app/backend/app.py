# backend/app.py
from flask import Flask, send_from_directory
from flask_restful import Api
# Optionally, you can remove CORS now since both frontend and backend share the same origin
# from flask_cors import CORS  
from config import Config
from models import db
from resources import GunplaListResource, GunplaResource
import os

def create_app(config_class=Config):
    # Set the static folder to the built frontend directory
    app = Flask(__name__, static_folder='../frontend/dist', static_url_path='')
    app.config.from_object(config_class)
    
    # (Optional) Remove or disable CORS as it's not needed for same-origin requests
    # CORS(app)
    
    # Initialize the database and create tables if needed
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # Register API resources
    api = Api(app)
    api.add_resource(GunplaListResource, '/gunplas')
    api.add_resource(GunplaResource, '/gunplas/<int:gunpla_id>')

    # Route to serve the frontend:
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve(path):
        # If the requested file exists in the build directory, serve it
        if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
            return send_from_directory(app.static_folder, path)
        # Otherwise, serve index.html (for client-side routing)
        return send_from_directory(app.static_folder, 'index.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0')