from flask_restful import Resource, reqparse
from models import db, Gunpla

# Configure request parser to expect JSON input
gunpla_parser = reqparse.RequestParser()
gunpla_parser.add_argument('name', type=str, required=True, help="Name field is required.", location='json')
gunpla_parser.add_argument('series', type=str, required=True, help="Series field is required.", location='json')
gunpla_parser.add_argument('grade', type=str, required=True, help="Grade field is required.", location='json')
gunpla_parser.add_argument('scale', type=str, location='json')


class GunplaListResource(Resource):
    def get(self):
        gunplas = Gunpla.query.all()
        return [gunpla.to_dict() for gunpla in gunplas], 200

    def post(self):
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


class GunplaResource(Resource):
    def get(self, gunpla_id):
        # Use Session.get() instead of Query.get()
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