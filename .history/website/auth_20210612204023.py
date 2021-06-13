from flask import Blueprint, render_template


auth = Blueprint('auth', __name__)


@auth.route('login')
def index():
    return "<h1>Login Page</h1>"

@auth.route('logout')
def index():
    return "<h1>Logout Page</h1>"

@auth.route('login')
def index():
    return "<h1>this is the home page for auth</h1>"

@auth.route('login')
def index():
    return "<h1>this is the home page for auth</h1>"

