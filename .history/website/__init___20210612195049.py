from flask import Flask


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = "adsf phiasdhf oa"
    
    from .usersController import user
    
    app.()
    
    return app

