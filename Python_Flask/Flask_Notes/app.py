from flask import Flask

# Flask ka ek app object banana
app = Flask(__name__)

# Jab koi homepage par aaye (/) toh yeh chalao
@app.route("/")
def home():
    return "<h1>Noor Mustaafa!</h1>"

# Website ko run karne ke liye
if __name__ == "__main__":
    app.run(debug=True)