from flask import Blueprint, render_template

users = Blueprint('users', __name__)


# https://localhost:5000/users/
# https://localhost:5000/users

@users.route('/')
def users_home():
    return "<h1>Welcome to the users' Home page</h1>"

# https://localhost:5000/users/login


@users.route('/login/id')
def users_login(id):

    notes = get(user_note.id)
    return render_template("login.html", notes=[{}, {}, {}, {}])


{% for note in notes %}
    <h1>{note.title}</h1
{% endpoint%}