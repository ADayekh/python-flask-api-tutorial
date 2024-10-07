from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
     {"label": "My first take", "done": True},
    
]

@app.route('/todos', methods=['GET'])
def hello_world(): 
     json_text = jsonify(todos), 200
     return json_text


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    json_text = jsonify(todos), 200
    return json_text

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.remove(todos[position])
    print("This is the position to delete:", position)
    json_text = jsonify(todos), 200
    return json_text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)