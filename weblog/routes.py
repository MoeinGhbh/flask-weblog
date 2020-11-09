from flask import Flask, render_template, request
from weblog import app

@app.route('/')
def index():
    return render_template('home.html')

