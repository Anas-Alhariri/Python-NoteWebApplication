from flask import Blueprint, render_template


auth = Blueprint('auth', __name__)


@auth.route('')
def index():
    return "<h1>this is the home page for auth</h1>"
