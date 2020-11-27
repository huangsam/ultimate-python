from flask import Flask
import flask
app = Flask(__name__)

@app.route("/")
def main_page():
    return app.send_static_file('readme.html')

@app.route('/ultimatepython/syntax/<filename>')
def serve_python_file(filename):
    return app.send_static_file(filename)

