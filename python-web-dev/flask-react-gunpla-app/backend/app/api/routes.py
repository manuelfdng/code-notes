from flask_restful import Resource
from app.models.gunpla import Gunpla
from app.utils.request_parser import gunpla_parser
from app.models import db

class GunplaListResource(Resource):
    def get(self):
        gunplas = Gunpla.query.all()
        return [gunpla.to_dict() for gunpla in gunplas], 200

    def post(self):
        try:
            args = gunpla_parser.parse_args()
            new_gunpla = Gunpla(
                name=args['name'],
                series=args['series'],
                grade=args['grade'],
                scale=args.get('scale')
            )
            db.session.add(new_gunpla)
            db.session.commit()
            return new_gunpla.to_dict(), 201
        except Exception as e:
            # Return validation errors as is since they're already formatted correctly
            if hasattr(e, 'data') and isinstance(e.data, dict):
                return e.data, 400
            return {"message": str(e)}, 400

class GunplaResource(Resource):
    def get(self, gunpla_id):
        gunpla = db.session.get(Gunpla, gunpla_id)
        if gunpla is None:
            return {'message': 'Gunpla model not found'}, 404
        return gunpla.to_dict(), 200

    def put(self, gunpla_id):
        gunpla = db.session.get(Gunpla, gunpla_id)
        if gunpla is None:
            return {'message': 'Gunpla model not found'}, 404
        
        args = gunpla_parser.parse_args()
        gunpla.name = args['name']
        gunpla.series = args['series']
        gunpla.grade = args['grade']
        gunpla.scale = args.get('scale')
        db.session.commit()
        return gunpla.to_dict(), 200

    def delete(self, gunpla_id):
        gunpla = db.session.get(Gunpla, gunpla_id)
        if gunpla is None:
            return {'message': 'Gunpla model not found'}, 404
        db.session.delete(gunpla)
        db.session.commit()
        return {'message': 'Gunpla model deleted successfully'}, 200

def initialize_routes(api):
    api.add_resource(GunplaListResource, '/gunplas')
    api.add_resource(GunplaResource, '/gunplas/<int:gunpla_id>')