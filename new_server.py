from random import randint
from flask import Flask
from flask import jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return get_output()

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)

"""
{
	"actions": [
		{
			"say": "Couldn't understand, please repeat the question"
		},
		{
			"listen": true
		}
	]
}
"""
def get_joke():
    jokes = open("jokes.txt", "r")
    jokes = jokes.readlines()
    return jokes[randint(0,len(jokes)-1)]

def get_output():
    joke = get_joke()
    joke = "\""+ joke + "\""
    out = "{\"actions\":[{\"say\":" +joke + "},{\"listen\":true}]}"
    return out