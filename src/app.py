from flask import Flask, jsonify, request

app= Flask(__name__)
#dummy data
todos = [
    { "label": "My first task", "done": False, "id": 1 },
    { "label": "My second task", "done": False, "id": 2 },
]


@app.route('/', methods=['GET'])
def hello_world():

    return '<h1>Hello World!</h1>'

@app.route('/todos', methods=['GET'])
def get_todos():
    
    response ={
        'message':"sending your list of todos",
        'todos': todos,
    }
    return jsonify(response), 200

@app.route('/todos', methods=['POST'])
def post_new_todos():
    request_body = request.json
    print("Received new POST request", request_body)

    todos.append(request_body)
    response= {
        'message': "received a post request",
        'todos': "todos",
     }
    return jsonify(request_body)

    


@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    for todo in todos:
        if todo.get('id') == id:
         todos.remove(todo)

    response = {
    'message': f'Received request to DELETE for id{id}',
    'todos': todos
    }
    return jsonify(response), 200


    





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)

