from flask import Blueprint, render_template


auth = Blueprint('auth', __name__)


@auth.route('login')
def login():
    return "<h1>Login Page</h1>"

@auth.route('logout')
def index():
    return "<h1>Logout Page</h1>"

@auth.route('sign-up')
def index():
    return "<h1>Sign up Page</h1>"
