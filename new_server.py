
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
    return "Why did the chicken cross the road? To get to the other side"
@app.route('/<id>')
def get_output(id):
    joke = get_joke()
    joke = repr(joke)
    out = "{\"actions\":[{\"say\":" +joke + "},{\"listen\":true]}"
    return out