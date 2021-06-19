from flask import Blueprint, render_template, request


auth = Blueprint('auth', __name__)


@auth.route('login', methods=['GET', 'POST'])
def login():
    # if request.method == 'POST':
    #     print("This was a post request")
    # else:
    #     print("This was a get request")
    
    return render_template("login.html")

@auth.route('logout')
def logout():
    return "<h1>Logout Page</h1>"

@auth.route('sign-up')
def sign_up():
    return "<h1>Sign up Page</h1>"