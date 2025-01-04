# runs the website

from flask import Flask, render_template
app = Flask(__name__)  # runs app with root path of module


# Main page
@app.route('/')
def home():
    return render_template('home.html') 


# test page
@app.route('/test')
def home2():
    return render_template('home.html')


# won't run server when imported as module
if __name__ == '__main__':
    app.run(debug=True)
