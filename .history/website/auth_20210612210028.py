from flask import Blueprint, render_template


auth = Blueprint('auth', __name__)


@auth.route('login')
def login():
    return 

@auth.route('logout')
def logout():
    return "<h1>Logout Page</h1>"

@auth.route('sign-up')
def sign_up():
    return "<h1>Sign up Page</h1>"
