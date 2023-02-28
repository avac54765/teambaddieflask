from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime

from model.workouts import workout

workout_api = Blueprint('workout_api', __name__,
                   url_prefix='/api/workout')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html

api = Api(workout_api)

# create the API for ISPE
class workoutAPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            # setting parameters for garbage data
            ''' Avoid garbage in, error checking '''
            # validate name
            name3 = body.get('name3')
            if name3 is None or len(name3) < 2:
                return {'message': f'Name is missing, or is less than 2 characters'}, 211
            # validate uid
            id = body.get('id')
            duration = body.get('duration')
            if duration is None or not int:
                return {'message': f'Duration is missing, or is not an integer'}, 212
            date = body.get('date')
            type = body.get('type')
            if duration is None or len(duration) > 2:
                return {'message': f'grade is missing, or is not a single letter'}, 213
            # uid = body.get('uid')
            uid = str(datetime.now()) # temporary UID that is unique to fill garbage data
            if uid is None or len(uid) < 2:
                return {'message': f'User ID is missing, or is less than 2 characters'}, 214

            from model.workouts import workout
            io = workout(id=id,
                      uid=uid,
                      name3=name3,
                      duration=duration,
                      date=date,
                      type=type,
                    )
            

            
            ''' #2: Key Code block to add user to database '''
            # create user in database
            workout = io.create()

            # success returns json of user
            if workout:
                return jsonify(workout.read())
            # failure returns error
            return {'message': f'Processed {name3}, either a format error or User ID {uid} is duplicate'}, 215

    class _Read(Resource):
        def get(self):
            workouts = workout.query.all()    # read/extract all users from database
            json_ready = [workout.read() for workout in workouts]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')