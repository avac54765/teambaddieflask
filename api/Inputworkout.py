import json
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime

from model.Inputworkouts import Inputworkout

Inputworkout_api = Blueprint('Inputworkout_api', __name__,
                   url_prefix='/api/Inputworkout')

api = Api(Inputworkout_api)

# API docs https://flask-restful.readthedocs.io/en/latest/api.html

class InputworkoutAPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate exercise type
            exerciseType = body.get('exerciseType')
            if exerciseType is None or len(exerciseType) < 2:
                return {'message': f'Input Exercise Type'}, 210
            # validate uid
            id = body.get('id')
            uid = str(datetime.now()) # temporary UID that is unique to fill garbage data
            if uid is None or len(uid) < 2:
                return {'message': f'User ID is missing, or is less than 2 characters'}, 212

            sets = body.get('sets')
            if sets is None or not int:
                return {'message': f'Input number of sets (must be integer)'}, 213
            reps = body.get('reps')
            if reps is None or len(reps) < 0:
                return {'message': f'Input number of repetitions (must be integer)'}, 214

            from model.Inputworkouts import Inputworkout

            io = Inputworkout(id=id,
                            uid=uid,
                            exerciseType=exerciseType,
                            sets=sets,
                            reps=reps,
                        )
            
            Inputworkout = io.create()

            # success returns json of user
            if Inputworkout:
                return jsonify(Inputworkout.read())
            # failure returns error
            return {'message': f'Processed {exerciseType}, a format error or User ID {uid} is duplicate'}, 215
    
    class _Read(Resource):
        def get(self):
            Inputworkouts = Inputworkout.query.all()    # read/extract all users from database
            json_ready = [Inputworkout.read() for Inputworkout in Inputworkouts]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')