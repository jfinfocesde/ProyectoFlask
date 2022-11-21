from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/test')
def login():
    return render_template("auth/login.html")

if __name__ == "__main__":
    app.run(debug=True, port=3000)