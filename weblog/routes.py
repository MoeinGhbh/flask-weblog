from flask import Flask, render_template, request
from weblog import app
from weblog.forms import RegistrationForm, LoginForm


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/registration', methods=['get', 'post'])
def registration():
    reg_form = RegistrationForm()
    return render_template('registration.html', form=reg_form)


@app.route('/login', methods=['get', 'post'])
def login():
    login_form = LoginForm()
    return render_template('login.html', form=login_form)
