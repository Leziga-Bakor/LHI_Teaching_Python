from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')  #127.0.0.1:5000
def index():
    name = 'nnamdi'
    l = list(name)
    dictname = {'age':23}
    user_logged_in = True
    return render_template('home.html',name=name, l=l, dictname=dictname, user_logged_in=user_logged_in)



@app.route('/about') #127.0.0.1:5000/about
def info():
    return render_template('about.html')

@app.route('/user/<name>') #127.0.0.1:5000/user/<name>
def person_page(name):
    
    return f'<h1> This is a page for {name}'

if __name__ == '__main__':
    app.run(debug=True)

