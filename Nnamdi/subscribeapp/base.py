from flask import Flask, render_template, request

app = Flask(__name__)
# Home -> Subscribe page -> thankyou page

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/subscribe_form')
def subscribe():
    return render_template('subscribe.html')

@app.route('/thank_you')
def thank_you():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('thankyou.html',first=first,last=last)


if __name__ == '__main__':
    app.run(debug=True)