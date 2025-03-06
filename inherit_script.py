# Inheriting the properties of the layout page
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/end')
def end():
    return render_template('end.html')

app.run(port=5005)