#!flask/bin/python
from flask import Flask
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


@app.route("/<id>")
def get_output(id):
    joke = get_joke()
    joke = "\""+ joke + "\""
    out = "{\"actions\":[{\"say\":" +joke + "},{\"listen\":true}]}"
    return out