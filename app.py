from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', index = 'active')


@app.route('/projects')
def projects():
    return render_template('projects.html', projects = 'active')


