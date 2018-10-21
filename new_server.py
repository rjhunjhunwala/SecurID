f#!flask/bin/python
from flask import Flask, jsonify
from random import randint
app = Flask(__name__)

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


@app.route('/', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': task})

if __name__ == '__main__':
    app.run(debug=True)


def get_output():
    joke = get_joke()
    joke = "\""+ joke + "\""
    out = "{\"actions\":[{\"say\":" +joke + "},{\"listen\":true}]}"
    return out