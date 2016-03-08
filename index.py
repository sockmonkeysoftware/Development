#================================================================
# - Sock Monkey Suduko Main Page Router				-
#----------------------------------------------------------------
#================================================================
from bottle import request, response
from bottle import default_app, run, route
from bottle import get, put, post, request, template
from bottle import static_file
import json

import example_board

#================================================================
# - A correct board for temporary UI testing...
#================================================================

@get('/')
def app():
    return template('index', board=example_board.revealed_cells)
    
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

if __name__ == "__main__":
    run(reloader = True, host="0.0.0.0")
else:
    application = default_app()
