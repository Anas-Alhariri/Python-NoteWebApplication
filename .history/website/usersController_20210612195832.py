from flask import Blueprint, render_template

users = Blueprint('users', __name__)


# https://localhost:500/users/
# https://localhost:500/users

@users.route('/')
def users_home():
    return "<h1>Welcome to the users' Home page</h1>"

@users.route('/login')
def users_home():
    return render_template("login.html")

