# Setting up modules
from cohere_rest import generateTasks
from flask import Flask, jsonify, request
# from flask_restful import Api, Resource

app = Flask(__name__)

# Request: category (string), Response: tasks (array of strings)

# RESTful API
@app.route('/category/<string:category>/', methods=['GET'])
def cohere_run_m(category):
    # print(category)
    return jsonify(generateTasks(category))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)