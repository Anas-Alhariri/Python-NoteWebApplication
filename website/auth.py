from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import login_user, login_required, logout_user, current_user

from . import db

auth = Blueprint("auth", __name__)


@auth.route("login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        print("This was a post request")
        form_data = request.form
        email = form_data.get("email").lower()
        password = form_data.get("password")

        if len(email) < 3:
            flash("Email address can't be less than 3 characters", category="error")
        elif "@" not in email:
            flash("Email address must have a '@' sign.", category="error")
            print("Email doesn't have @")
        elif len(password) < 7:
            flash("Password should be greater than 7 characters", category="error")
        else:
            user = User.query.filter_by(email=email).first()
            if user:
                if check_password_hash(user.password, password):
                    flash("Logged in successfully!", category="success")
                    login_user(user, remember=True)
                    return redirect(url_for("views.home"))
                else:
                    flash("Password is incorrect, please try again!", category="error")
            else:
                flash(
                    f"Couldn't find a user with the email address of {email}, please try with different email!",
                    category="error",
                )

                print(
                    f"""
                    Email: {email}
                    Password: {password}
                    """
                )
    else:
        print("This was a get request")

    return render_template("login.html", user=current_user)


@auth.route("logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


@auth.route("sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        form_data = request.form
        first_name = form_data.get("firstName")
        email = form_data.get("email").lower()
        password1 = form_data.get("password1")
        password2 = form_data.get("password2")
        print("Active")
        if len(first_name) < 2:
            flash("User name is less than 2 characters", category="error")
        elif len(email) < 3:
            flash("User email is less than 3 characters", category="error")
        elif len(password1) < 7:
            flash("Password should be greater than 7 characters", category="error")
        elif password1 != password2:
            flash("Passwords are not identical", category="error")
        else:
            # add a user to the database
            user = User.query.filter_by(email=email).first()
            if user:
                flash(
                    f"A user with {email} is already exists! Please, try with different email address.",
                    category="error",
                )
            else:
                password1 = generate_password_hash(password1, method="sha256")
                new_user = User(email=email, first_name=first_name, password=password1)

                db.session.add(new_user)
                db.session.commit()

                print(
                    f"""
                    First Name: {first_name}
                    Email: {email}
                    Password1: {password1}
                    Password2: {password2}
                    """
                )

                flash("User account was created successfully", category="success")
                login_user(new_user, remember=True)
                return redirect(url_for("views.home"))
    return render_template("sign_up.html", user=current_user)
