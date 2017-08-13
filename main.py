"""
Purpose create a User-signup using previously taught skills

STEP 1 Planning and Analysis

STEP 2 Pseudocode

STEP 3 REVIEW previous assignment

STEP 4 Code main.py and html templates
"""

from flask import Flask, request, redirect, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/welcome", methods=["POST"])
def welcome():

    #Create an algorithm to validate: Username, Password, Verify Password and Email
    # Finally pass the Username value through to welcome page.

    username = request.form["username"]
    password = request.form["password"]
    verify = request.form["verify"]
    email = request.form["email"]

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    if len(username) < 3 or len(username) > 20 or " " in username:
        username_error = "Invalid Username"
    
    if len(password) < 3 or len(password) > 20 or " " in password:
        password_error = "Invalid Password Length"

    #if len(verify) < 3 or len(verify) > 20 or " " in verify:
    if username != verify:
        username_error = "Passwords do not match"    

    if "." not in email and "@" not in email:
        email_error = "Invalid Email"

    if not username_error and not password_error and not verify_error:
        username = str(username)
        return redirect("/welcome?username{0}".format(username))
    """
    else: 
        template = jinja_env.get_template("welcome.html")
        return render_template("welcome.html",)
    

@app.route("/validate-time", methods=["POST"])
def validate_time():

    hours = request.form["hours"]
    minutes = request.form["minutes"]

    hours_error = ""
    minutes_error = ""

    if not is_integer(hours):
        hours_error = 'Not a valid integer'
    else:
        hours = int(hours)
        if hours > 23 or hours < 0:
            hours_error = "Hour value out of range (0-23)"    

    if not is_integer(minutes):
        minutes_error = 'Not a valid integer'    
    else:
        minutes = int(minutes)
        if minutes > 59 or minutes < 0:
            minutes_error = "Minutes value out of range (0-59)"
    
    if not minutes_error and not hours_error:
        time = str(hours) + ':' + str(minutes)
        return redirect('/valid-time?time={0}'.format(time))
    else:
        template = jinja_env.get_template("time_form.html")
        return render_template("time_form.html", 
            hours_error=hours_error, 
            minutes_error=minutes_error,
            hours=hours,
            minutes=minutes)

@app.route("/valid-time")
def valid_time():
    time = request.args.get('time')
    return '<h1>You submitted {0}. Thanks for submitting a valid time!</h1>'.format(time)            
"""


if __name__ == "__main__":
    app.run()
