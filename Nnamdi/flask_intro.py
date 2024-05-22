from flask import Flask

app = Flask(__name__)

@app.route('/')  #127.0.0.1:5000
def index():
    return '<h1>Hello Nnamdi</h1>'

@app.route('/about') #127.0.0.1:5000/about
def info():
    return '<h1>  i am learning Flask for web development </h1>'

@app.route('/user/<name>') #127.0.0.1:5000/user/<name>
def person_page(name):
    
    return f'<h1> This is a page for {name}'

if __name__ == '__main__':
    app.run(debug=True)

