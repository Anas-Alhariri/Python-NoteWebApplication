from flask import Blueprint, render_template


views = Blueprint('views', __name__)

@views.route('/')
def index():
    return "<h1>this is the home page for views</h1>"