from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/login')

def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # TODO: Check username and password against database or other authentication system
        if username != 'admin' or password != 'password':
            error = 'Invalid username or password. Please try again.'
        else:
            return 'Logged in successfully!'
    return render_template('login.html', error=error)

  