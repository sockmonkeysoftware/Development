#================================================================
# - Sock Monkey Suduko Main Page Router				-
#----------------------------------------------------------------
#================================================================
from bottle import run, route, view, app, hook
from bottle import get, put, post, request, redirect, template
from bottle import static_file, error, debug
from beaker.middleware import SessionMiddleware
import json

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/src/Controller")
from BoardController import *

import example_board

#================================================================
# - A correct board for temporary UI testing...
#================================================================

# Beaker Session Options and Initialization
app = app()
session_opts = {
    'session.auto': True,
    'session.cookie_expires': True,
    'session.encrypt_key': 'please use a random key and keep it secret!',
    'session.timeout': 3600 * 24,  # 1 day
    'session.type': 'cookie',
    'session.validate_key': True,
    'session.httponly': True,
}

app = SessionMiddleware(app, session_opts)

#================================================================
# - Authentication Route Decorator
#================================================================
# Example Use: 
#
# @get('/')
# @validate
# def app():

def validate(func):
    @wraps(func)
    def call(*args, **kwargs):
        sess_id = request.cookies.get('beaker.session.id', False)
        if not sess_id:
            return redirect('/login')
        sess = request.environ.get('beaker.session')
        if 'board' not in sess:
            return redirect('/login')
        return func(*args, **kwargs)
    return call

#================================================================
# - Application Routes
#================================================================

@get('/')
def index():
    return template('index', board=example_board.revealed_cells)
    
@get('/new')
def new_game():
    play()
    
    sess = request.environ.get('beaker.session')
    print(sess['game_board'])
    
@post('/update')
def update_handler():
    correct = False
    
    try:
        try:
            cell_id = request.forms.get('id')
            value = request.forms.get('value')
        except:
            raise ValueError
        
        '''
        if data is None:
            raise ValueError
        
        try:
            cell_id = data['id']
            value = data['value']
        except (TypeError, KeyError):
            raise ValueError
        if name in _names:
            raise KeyError
        '''

    except ValueError:
        response.status = 400
        return
    
    '''
    except KeyError:
        response.status = 409
        return
    '''

    print(cell_id, value)

    if example_board.complete_board[cell_id] == int(value):
        correct = True
    
    # return 200 Success
    response.headers['Content-Type'] = 'application/json'
    return json.dumps({'id': cell_id,'correct': correct})

@route('/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static/')

def main():
    debug(True)
    run(app=app, quiet=False, reloader=True)
    
if __name__ == "__main__":
    main()
