#================================================================
# - Sock Monkey Suduko Main Page Router				-
#----------------------------------------------------------------
#================================================================
from bottle import run, route, view, app, hook
from bottle import get, put, post, request, redirect, template
from bottle import static_file, error, debug
from functools import wraps
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
# - Valid Game Route Decorator
#================================================================

def validate(func):
    @wraps(func)
    def call(*args, **kwargs):
        if not game_exists():
            return redirect('/new')
        return func(*args, **kwargs)
    return call

#================================================================
# - Application Routes
#================================================================

@route('/')
@validate
def index():
    return resume()
    
@route('/new')
def new_game():
    if game_exists(): 
        redirect('/')
    return play()
    
@post('/update')
@validate
def update_handler():
    return update()

@route('/end')
@validate
def end_game():
    return end()

@route('/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static/')

def main():
    debug(True)
    run(app=app, quiet=False, reloader=True)
    
if __name__ == "__main__":
    main()
