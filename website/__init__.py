from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

#!! Initiating an object from the "SQLALCHEMY" class:
db = SQLAlchemy()

#!! Storing the name of our database file in a constant variable to be used later to build our database connection string:
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "adsf phiasdhf oa"

    #!! Creating the database connection string:
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"

    #!! Initiating the database with the app that will communicate with it (The flask 'app'/[Flask object]):
    db.init_app(app)

    # from .usersController import users
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Note

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    create_database(app)

    # app.register_blueprint(users, url_prefix='/users')

    return app


def create_database(app):
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)
