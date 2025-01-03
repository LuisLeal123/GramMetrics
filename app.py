from flask import Flask 

# runs app with root path of module
app = Flask(__name__) 

# Main page
@app.route('/')
def home():
    return "Hello, World!"

# test page
@app.route('/test')
def home2():
    return "testing other homepage"

# won't run server when imported as module
if __name__ == '__main__':
    app.run(debug=True)
