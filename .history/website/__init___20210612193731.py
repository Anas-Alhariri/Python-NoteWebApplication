from flask import Flask


app = Flask(__name__)

app.config['SECRET_KEY'] = "adsf phiasdhf oa"


app.run(debug=True)
