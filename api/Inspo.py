import json
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource 
from datetime import datetime

from model.Inspos import Inspo

Inspo_api = Blueprint('Inspo_api', __name__,
                   url_prefix='/api/Inspo')

api = Api(Inspo_api)

class InspoAPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # check for bad data
            quote = body.get('quote')
            if quote is None or len(quote) < 2:
                return {'message': f'Quote is missing, or is less than 2 characters'}, 210
            
        
            uid = str(datetime.now()) # temporary UID that is unique to fill garbage data (in future would be a login)
            if uid is None or len(uid) < 2:
                return {'message': f'User ID is missing, or is less than 2 characters'}, 214
            id = body.get('id')

            from model.Inspos import Inspo
            uo = Inspo(uid=uid,
                       quote=quote,
                       id=id)
            
        
            ''' #2: Key Code block to add user to database '''
            # create quote in database
            quote = uo.create()

            # json data of quote
            if quote:
                return jsonify(quote.read())
            return {'message': f'Processed {quote}, either a format error, quote duplicate, or User ID {uid} is duplicate'}, 210 # error message here

    class _Read(Resource):
        def get(self):
            quotes = Inspo.query.all()    # read quotes from database
            json_ready = [quote.read() for quote in quotes]  # turn data into readable json
            return jsonify(json_ready) 

    # RESTapi endpoints
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')