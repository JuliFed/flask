from flask import Flask
from flask import jsonify
from flask import request
import json
from  flask import Response
from werkzeug.exceptions import NotFound

tasks = {
    'last-id': 2,
    'todo': [
        {
            "id": 1,
            "title": "Learn Python",
            "description": "",
            "done": False
        },
        {
            "id": 2,
            "title": "Prigitovit borsh",
            "description": "Vkusniy borsh! Deti hotyat est",
            "done": False
        }
    ]
}


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/todo/api/tasks')
def get_tasks():
    return jsonify({"tasks": tasks['todo']})


@app.route('/todo/api/tasks/<int:task_id>')
def get_one_task(task_id):
    for task in tasks['todo']:
        if task['id'] == task_id:
            return jsonify(task)
    raise NotFound


@app.route('/todo/api/tasks', methods=['POST'])
def create_task():
    new_id = tasks['last-id']+1
    tasks['last-id'] = new_id
    data = request.get_json()

    new_task = {
        'id': new_id,
        'title': data['title'],
        'description': data['description'],
        'done': False
    }
    tasks['todo'].append(new_task)
    return Response(json.dumps(new_task), status=201, mimetype='application/json')
    # return jsonify(new_task), 201

