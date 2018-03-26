import sys
import os
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/FlaskApp5/")

def application(environ, start_response):
    for key in ['FLASK_KEY_2']:
        os.environ[key] = environ.get(key, '')
    from FlaskApp4 import app as _application
    return _application(environ, start_response)
    
    
#this secret_key loads after config.py Config
#os.environ['FLASK_KEY'] = os.environ['FLASK_KEY_1']
#application.secret_key = 'qwerty'
#os.environ['FLASK_KEY']
