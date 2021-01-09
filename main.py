from flask import Flask

app = Flask(__name__)


@app.route("/")
def homepage():
    return "Home Page"


    
app.run(host='0.0.0.0', debug=True)
