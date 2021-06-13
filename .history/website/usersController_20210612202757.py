from flask import Blueprint, render_template

users = Blueprint('users', __name__)


# https://localhost:5000/users/
# https://localhost:5000/users

@users.route('/')
def users_home():
    return "<h1>Welcome to the users' Home page</h1>"

# https://localhost:5000/users/login


@users.route('/login')
def users_login():
    return render_template("login.html")


# https://localhost:5000/users/notes
@users.route('/notes/<id>')
def users_notes(id):
    notes = db.query
    return "this is the notes page #" + id
