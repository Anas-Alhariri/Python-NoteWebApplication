from flask import Blueprint

users = Blueprint('users', __name__)


# 

@users.route('/users')
def users_home():
    return "<h1>Welcome to the users' Home page</h1>"