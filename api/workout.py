from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime

from model.workouts import workout

workout_api = Blueprint('workout_api', __name__,
                   url_prefix='/api/workout')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(workout_api)

class workoutAPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate name
            fname = body.get('fname')
            if fname is None or len(fname) < 2:
                return {'message': f'Name is missing, or is less than 2 characters'}, 211
            # validate uid
            lname = body.get('lname')
            if lname is None or len(lname) < 2:
                return {'message': f'Name is missing, or is less than 2 characters'}, 212
            # validate uid
            id = body.get('id')
            
            duration = body.get('duration')
            if duration is None or not int:
                return {'message': f'Duration is missing, or is not an integer'}, 214
            date = body.get('date')
            workouttype = body.get('workouttype')
            if workouttype is None or len(workouttype) > 1:
                return {'message': f'grade is missing, or is not a single letter'}, 215
             # uid = body.get('uid')
            uid = str(datetime.now())
            if uid is None or len(uid) < 2:
                return {'message': f'User ID is missing, or is less than 2 characters'}, 216

            from model.workouts import workout
            uo = workout(id=id, 
                      uid=uid,
                      fname=fname,
                      lname=lname,
                      date=date,
                      duration=duration,
                      workouttype=workouttype)
            

            
            ''' #2: Key Code block to add user to database '''
            # create user in database
            workout = uo.create()

            # success returns json of user
            if workout:
                return jsonify(workout.read())
            # failure returns error
            return {'message': f'Processed {fname}, either a format error or User ID {uid} is duplicate'}, 217

    class _Read(Resource):
        def get(self):
            workouts = workout.query.all()    # read/extract all users from database
            json_ready = [workout.read() for workout in workouts]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')