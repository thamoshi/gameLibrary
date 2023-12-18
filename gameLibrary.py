from flask import Flask, render_template

app = Flask(__name__)


@app.route('/home')
def helloWorld():
    return render_template('home.html')


app.run()
