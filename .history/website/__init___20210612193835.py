from flask import Flask


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = "adsf phiasdhf oa"
    
    return app

if __name__ == '__main__':
    app.run(debug=True)
