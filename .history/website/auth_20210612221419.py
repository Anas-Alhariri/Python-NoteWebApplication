from flask import Blueprint, render_template, request


auth = Blueprint('auth', __name__)


@auth.route('login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print("This was a post request")
        form_data = request.form
        email'))
        password
    else:
        print("This was a get request")
    
    
    
    return render_template("login.html")

@auth.route('logout')
def logout():
    return "<h1>Logout Page</h1>"

@auth.route('sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        form_data = request.form
        print(form_data)
        print("That was a post request")
    return render_template("sign_up.html")