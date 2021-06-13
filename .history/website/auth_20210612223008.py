from flask import Blueprint, render_template, request


auth = Blueprint('auth', __name__)


@auth.route('login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print("This was a post request")
        form_data = request.form
        email = form_data.get('email')
        password = form_data.get('password')
        print(f"Email: {email}\nPassword: {password}")
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
        first_name = form_data.get('firstName')
        email = form_data.get('email')
        password1 = form_data.get('password1')
        password2 = form_data.get('password2')
        
        if len(email) < 4:
            pass
        elif len(first_name) < 2:
            pass
        elif password1 != password2:
            pass
        elif len(password1)
        
        print(f"""
              First Name: {first_name}
              Email: {email}
              Password1: {password1}
              Password2: {password2}
              """)

        # print(form_data)
        # print("That was a post request")
    return render_template("sign_up.html")
