from flask import Flask


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = "adsf phiasdhf oa"
    
    # from .usersController import users
    
    from .views import views
    
    app.register_blueprint(views, url_prefix='/')
    
    # app.register_blueprint(users, url_prefix='/users')
    
    return app

