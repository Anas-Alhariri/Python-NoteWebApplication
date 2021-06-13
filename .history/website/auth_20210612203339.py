from flask import Blueprint, render_template


Auths = Blueprint('Auths', __name__)


@Auths.route('/')
def index():
    return "<h1>this is the home page for Auths</h1>"
