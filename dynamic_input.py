from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
  return '<h1>Welcome to FLASK Workshop</h1>'

@app.route('/name/<uname>')
def username(uname):
  return f"<h2>Hello {uname} welcome to pythonic way to implement a website !!</h2>"

# Running the application
app.run(port=5006)