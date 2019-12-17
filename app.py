import helper
from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello world'

@app.route('/item/new', methods=['POST'])
def add_item():
    # Get item from the POST body
    req_data = request.get_json()
    item = req_data['item']

    # Add item to the list
    res_data = helper.add_to_list(item)

    # Return error if item not added
    if res_data is None:
        response = Response("{'error': 'Item is not added - " + item + "'}", status=400, mimetype='application/json')
        return response
    
    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')

    return response

@app.route('/items/all')
def get_all_items():
    # Get items from helper
    res_data = helper.get_all_items()


    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')
    
    return response

@app.route('/item/status', methods=['GET'])
def get_item():
    # Get parameter from the URL
    item_name = request.args.get('name')

    # Get items from the helper
    status = helper.get_item(item_name)

    # Return 404 if not found
    if status is None:
        response = Response("{'error': 'Item Not Found - %s'}" % item_name, status=400, mimetype='application/json')
        return response

    # Return status
    res_data = {
        'status': status
    }

    response = Response(json.dumps(res_data), status=200, mimetype='application/json')
    return response