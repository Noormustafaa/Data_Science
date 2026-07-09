from flask import Flask

app1 = Flask(__name__)


@app1.route("/")
def home():
    return "HomePage"


@app1.route("/about")
def about():
    return "About Page"


@app1.route("/contact")
def contact():
    return "Contact Page"


app1.run(debug=True)