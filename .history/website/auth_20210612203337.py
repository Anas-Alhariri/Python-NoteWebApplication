from flask import Blueprint, render_template


Au = Blueprint('Au', __name__)


@Au.route('/')
def index():
    return "<h1>this is the home page for Au</h1>"
