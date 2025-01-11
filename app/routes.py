from flask import Blueprint, render_template, jsonify, request

# all the routes
# flask manages url to functions and listens to gets/posts
# app = Flask(__name__) // this basically creates the app, but we need container for just routes
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/api/action', methods=['POST'])
def handle_button():
    # Get the action from the request body
    data = request.json
    action = data.get('action')

    # Handle different actions dynamically
    if action == 'greet':
        return jsonify({"message": "Hello, User!"})
    else:
        return jsonify({"message": "Unknown action"}), 400

@main.route("/<string:name>")
def test(name):
    name = name.capitalize()
    return render_template('home.html', name=name)

# register the routes in create_app()