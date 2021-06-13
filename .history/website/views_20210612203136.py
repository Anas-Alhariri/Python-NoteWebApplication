from flask import Blueprint, render_template


views = Blueprint('views', __name__)

@views.route('/')
def index():
    return "this is the home page for "