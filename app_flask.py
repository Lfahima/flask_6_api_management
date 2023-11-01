from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)


@app.route('/hello', methods=['GET'])
def hello_get():
    """
    This is an example hello world function that takes in a name and if it is not provided it uses Fahima
    ---
    parameters:
      - name: name
        in: query
        type: string
        required: false
        default: Fahima
    responses:
      200:
        description: Returns a JSON object with a message that says ```Hello `name`!```
    """
    name = request.args.get('name', 'Fahima')
    return jsonify({'message': f'Hello {name}!'})

if __name__ == '__main__':
    app.run(debug=True)