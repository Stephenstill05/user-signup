from flask import Flask, request, redirect, render_template
import cgi
import os


template_dir = os.path.join(os.path.dirname(__file__), 'templates')


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    
    return render_template('Homepage.html',user_error='',pass_error='',same_error='',email_error='')


def verified(var):
    if len(var) >= 3 and len(var) <= 20 and not ' ' in var:
        return True
    else:
        return False

def email_ver(letters):
    if len(letters) == 0:
        return True
    elif verified(letters) and '@' in letters and '.' in letters:
        return True
    else:
        return False

@app.route("/", methods=['POST'])
def signup():
    user = request.form['fullname']
    pass1 = request.form['password']
    pass2= request.form['verify-password']
    email= request.form['e-mail']


    user_error=''
    if len(user)==0:
        user_error='User Name is left blank'
    elif not verified(user):
        user_error='User Name needs to be 3-20 characters with no spaces'
    else:
        user = user

    pass_error=''
    if len(pass1)==0:
        pass_error = 'Password is left blank'
    elif not verified(pass1):
        pass_error='Password needs to be 3-20 characters with no spaces'
    else:
        pass1 = pass1

    same_error=''
    if pass1 != pass2:
        same_error='Passwords do not match'
    else:
        pass2=pass2

    email_error=''
    if email_ver(email)==False:
        email_error='Not a valid email between 3-20 characters with no spaces'
    else:
        email=email

    if not user_error and not pass_error and not same_error and not email_error:
        return render_template('Welcomepage.html',user=user)
    else:
        return render_template('Homepage.html',user_error=user_error,pass_error=pass_error,same_error=same_error,email_error=email_error)
app.run()