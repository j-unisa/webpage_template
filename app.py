from flask import Flask, render_template

# Creates a Flask application instance
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/first')
def first():
    return render_template("first.html")


@app.route('/second')
def second():
    return render_template("second.html")


@app.route('/third')
def third():
    return render_template("third.html")


# Ensures dev server only starts when script is executed directly
if __name__ == '__main__':
    app.run()
