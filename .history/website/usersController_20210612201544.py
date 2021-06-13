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

    notes = get(user_note.id)
    return render_template("login.html", notes=[{"id": 0, "title": '', "data":''}, {}, {}, {}])


note = {"id": 0, "title": '', "data": ''}

{% for note in notes %}
    <div class="" key=note.id>
        <h1>{{ note.title }}</h1>
        <p>{{ note.data }}</p>
    </div>
{% endfor %}
