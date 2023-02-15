import json
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime

from model.Inspos import Inspo

Inspo_api = Blueprint('Inspo_api', __name__,
                   url_prefix='/api/Inspo')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(Inspo_api)

class InspoAPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate name
            quote = body.get('quote')
            if quote is None or len(quote) < 2:
                return {'message': f'Quote is missing, or is less than 2 characters'}, 210
            # validate uid
            uid = body.get('uid')
            if uid is None or len(uid) < 2:
                return {'message': f'User ID is missing, or is less than 2 characters'}, 210
            id = body.get('id')

            from model.Inspos import Inspo
            uo = Inspo(uid=uid,
                       quote=quote,
                       id=id)
            

            # FOR INSPO PT 2
            #if quote is not None:
               #q.set_quote(quote)
            
            ''' #2: Key Code block to add user to database '''
            # create user in database
            quote = uo.create()

            # success returns json of user
            if quote:
                return jsonify(quote.read())
            # failure returns error
            return {'message': f'Processed {uid}, either a format error or User ID {uid} is duplicate'}, 210

    class _Read(Resource):
        def get(self):
            quotes = Inspo.query.all()    # read/extract all users from database
            json_ready = [quote.read() for quote in quotes]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')