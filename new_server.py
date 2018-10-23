#!flask/bin/python
from flask import Flask, jsonify
from flask_restful import Resource, Api
from random import randint
app = Flask(__name__)
api = Api(app)

def get_joke():
    jokes = open("jokes.txt", "r")
    jokes = jokes.readlines()
    return jokes[randint(0,len(jokes)-1)]

task = {
	"actions": [
		{
			"say": get_joke()
		},
		{
			"listen": True
		}
	]
}


class Sim(Resource):
    def get(self):
        return start()

def start():
    return jsonify(task)

api.add_resource(Sim)

if __name__ == '__main__':
    app.run(debug=True)


def get_output():
    joke = get_joke()
    joke = "\""+ joke + "\""
    out = "{\"actions\":[{\"say\":" +joke + "},{\"listen\":true}]}"
    return out