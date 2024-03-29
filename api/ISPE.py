from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime

from model.ISPEs import ISPE

ISPE_api = Blueprint('ISPE_api', __name__,
                   url_prefix='/api/ISPE')


api = Api(ISPE_api)

# create the API for ISPE
class ISPEAPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            # setting parameters for garbage data
            ''' Avoid garbage in, error checking '''
            # validate name
            name2 = body.get('name2')
            if name2 is None or len(name2) < 2:
                return {'message': f'Name is missing, or is less than 2 characters'}, 211
            # validate uid
            id = body.get('id')
            duration2 = body.get('duration2')
            if duration2 is None or not int:
                return {'message': f'Duration is missing, or is not an integer'}, 212
            date2 = body.get('date2')
            grade = body.get('grade')
            uid = str(datetime.now()) # temporary UID that is unique to fill garbage data
            if uid is None or len(uid) < 2:
                return {'message': f'User ID is missing, or is less than 2 characters'}, 214

            from model.ISPEs import ISPE
            io = ISPE(id=id,
                      uid=uid,
                      name2=name2,
                      duration2=duration2,
                      date2=date2,
                      grade=grade,
                    )
            

            
            ''' #2: Key Code block to add user to database '''
            # create user in database
            ISPE = io.create()

            # success returns json of user
            if ISPE:
                return jsonify(ISPE.read())
            # failure returns error
            return {'message': f'Processed {name2}, either a format error or User ID {uid} is duplicate'}, 215

    class _Read(Resource):
        def get(self):
            ISPEs = ISPE.query.all()    # read/extract all users from database
            json_ready = [ISPE.read() for ISPE in ISPEs]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')