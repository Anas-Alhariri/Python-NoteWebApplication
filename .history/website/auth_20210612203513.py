from flask import Blueprint, render_template


auths = Blueprint('auths', __name__)


@auths.route('/')
def index():
    return "<h1>this is the home page for auths</h1>"
