from flask import Flask
from flask import render_template, redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.jinja2')

if __name__ == '__main__':
    app.run()
