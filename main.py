from flask import Flask,redirect,url_for,render_template,request


app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('home.html')
    return render_template('home.html')

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


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)