# https://www.youtube.com/watch?v=fxavwHPJ36o
# https://palletsprojects.com/p/flask/
# https://stackoverflow.com/questions/37465506/jinja2-exceptions-templatenotfound
# https://www.tutorialspoint.com/flask/index.htm
# https://www.tutorialspoint.com/django/index.htm
import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')


@app.route('/about')
def about():
	return render_template('about.html')


if __name__ == "__main__":
	app.run(host=os.getenv('IP', '0.0.0.0'), 
					port=int(os.getenv('PORT',5000)),debug=True)