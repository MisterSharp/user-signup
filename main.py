from flask import Flask, request, redirect, render_template
import cgi
import os
import validators

app = Flask(__name__)

app.config['DEBUG'] = True

def not_blank(s):
    return bool(s and s.strip())


@app.route("/", methods=['POST','GET'])
def index():
    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""
    username = ""
    email = ""
    password = ""
    verify = ""

    if request.method == 'POST': #validing the form fields
        username = request.form['Username']
        email = request.form['Email']
        #is Username blank?
        if " " in request.form['Username']:
            username_error += "Spaces are not allowed in username."
        #is it between 3 & 20 characters?
        if len(request.form['Username']) < 3 or len(request.form['Username']) > 20:
            username_error += "Username must be between 3-20 characters"
        #is password blank?
        if " " in request.form['Password']:
            password_error += "Spaces are not allowed in the password"
        #is it between 3 & 20 characters?
        if len(request.form['Password']) < 3 or len(request.form['Password']) > 20:
            password_error += "Password must be between 3-20 characters"
        #do passwords match?
        if request.form['Verify'] != request.form['Password']:
            verify_error += "Passwords do not match"
        
        
        #if the Email field is not blank
        if not_blank(request.form['Email']) == True:
            #check to make sure its a valid e-mail
            if not validators.email(request.form['Email']):
                email_error = 'Enter a valid e-mail or leave blank'

    return render_template('sign-up.html', username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error, username=username, email=email, password=password, verify=verify)

@app.route("/welcome")
def valid():
    user = request.form['Username']
    return render_template('welcome.html', user=user)



app.run()