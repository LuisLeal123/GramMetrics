from flask import Blueprint, render_template

# all the routes
# flask manages url to functions and listens to gets/posts
# app = Flask(__name__) // this basically creates the app, but we need container for just routes
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route("/<string:name>")
def test(name):
    name = name.capitalize()
    #return f"hello, {name}"
    return render_template('home.html', name=name)

# register the routes in create_app()