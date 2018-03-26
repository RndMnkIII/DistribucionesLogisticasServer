#import sys
#import os
#import logging
#logging.basicConfig(stream=sys.stderr)
#sys.path.insert(0,"/var/www/FlaskApp4/")
from FlaskApp4 import app, db
from FlaskApp4.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'User':User, 'Post':Post}

