from flask import Flask, request, redirect, render_template
import cgi
import os


app = Flask(__name__)

app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('sign-up.html')

def validate():
    username_error = ''
    password_error = ''
    verify_error = ''

    
















app.run()