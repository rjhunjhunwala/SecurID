from random import randint
from flask import Flask

app = Flask(__name__)


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

@app.route('/<id>')
def get_output(id):
    joke = get_joke()
    joke = repr(joke)
    out = "{\"actions\":[{\"say\":" +joke + "},{\"listen\":true]}"
    return out