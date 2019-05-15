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



    
    
    
    if request.method == 'POST': #validing the form fields

        username = request.form['Username']
        email = request.form['Email']
        #is Username blank?
        if " " in request.form['Username']:
            username_error += "Spaces are not allowed in username."
        #is it between 3 & 20 characters?
        if len(request.form['Username']) < 3 or len(request.form['Username']) > 20:
            username_error += "Username must be between 3-20 characters"
        #do passwords match?
        #if request.form['']:
            #pass
        #if request.form['']
        
        
        #if the Email field is not blank
        if not_blank(request.form['Email']) == True:
            #check to make sure its a valid e-mail
            if not validators.email(request.form['Email']):
                email_error = 'Enter a valid e-mail or leave blank'

    return render_template('sign-up.html', username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error, username=username, email=email)



app.run()