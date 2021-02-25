import datetime

from flask import jsonify
from flask_restx import Resource, reqparse
from sqlalchemy.exc import InvalidRequestError
from FlaskModule import default_api_ns as api
from opentera.services.ServiceAccessManager import ServiceAccessManager, current_participant_client

# Parser definition(s)
get_parser = api.parser()


class QueryVersion(Resource):

    def __init__(self, _api, *args, **kwargs):
        Resource.__init__(self, _api, *args, **kwargs)
        self.module = kwargs.get('flaskModule', None)
        self.parser = reqparse.RequestParser()

    @api.expect(get_parser)
    @api.doc(description='To be documented '
                         'To be documented',
             responses={200: 'Success - To be documented',
                        500: 'Required parameter is missing',
                        501: 'Not implemented.',
                        403: 'Logged user doesn\'t have permission to access the requested data'})
    
    
    #@ServiceAccessManager.token_required
    def get(self):
        version = {'TeleopService': 
            {'version': '1.0.0'}
        }
        return version

