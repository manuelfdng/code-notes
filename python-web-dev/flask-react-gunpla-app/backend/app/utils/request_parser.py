from flask_restful import reqparse

# Configure the parser to bundle errors
gunpla_parser = reqparse.RequestParser(bundle_errors=True)
gunpla_parser.add_argument('name', type=str, required=True, help="Name field is required.", location='json')
gunpla_parser.add_argument('series', type=str, required=True, help="Series field is required.", location='json')
gunpla_parser.add_argument('grade', type=str, required=True, help="Grade field is required.", location='json')
gunpla_parser.add_argument('scale', type=str, location='json')