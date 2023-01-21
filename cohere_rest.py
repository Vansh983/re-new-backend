# Setting up modules
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import cohere

app = Flask(__name__)
api = Api(app)
co = cohere.Client('bPnEkiW2KeYyupinU83dcN1wKVp4w1Lo1zXx28dC')

# Skill = 'skill learning'
# fitness = fitness, academic = academic, wellness = wellness
prompt = f"""  
Give four unique wellness goals for me to do today, in a list.
""" 
# not sure if we need to finish with a -- here
# change category fitness to be {selection}

model = "command-medium-nightly" 
max_tokens = 50
temperature = 1.3 # this is the randomness, 0 is predictable, 5 is creative
 # this indicates the end of the prompt

# RESTful API
class StringArray(Resource):
    def get(self):
        response = co.generate(model = model, prompt = prompt, max_tokens = max_tokens, temperature = temperature,)
        tasks = response.generations[0].text
        task_list = [task.strip()[2:] for task in tasks.split("\n")]
        return jsonify(task_list)

api.add_resource(StringArray, '/')

if __name__ == '__main__':
    app.run(debug=True)
